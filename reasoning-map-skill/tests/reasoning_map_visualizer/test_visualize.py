import json
import io
import contextlib
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.reasoning_map_visualizer import (
    GraphValidationError,
    build_render_graph,
    SelectionOptions,
    load_graph,
    select_graph,
)


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "sample_graph.json"


class LoaderTest(unittest.TestCase):
    def test_fixture_includes_visibility_and_status_cases(self):
        graph = load_graph(FIXTURE_PATH)

        node_titles = {node["title"] for node in graph["nodes"]}
        edge_ids = {edge["id"] for edge in graph["edges"]}

        self.assertIn("Muted claim", node_titles)
        self.assertIn("Hidden risk", node_titles)
        self.assertIn("Rejected option", node_titles)
        self.assertIn("edge.dangling", edge_ids)

    def test_load_graph_normalizes_optional_fields(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            graph_path = Path(tmpdir) / "minimal_graph.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "minimal.graph",
                        "title": "Minimal graph",
                        "nodes": [{"id": "problem.one", "kind": "problem", "title": "Problem"}],
                        "edges": [{"id": "edge.one", "from": "problem.one", "to": "problem.one", "type": "relates_to"}],
                    }
                ),
                encoding="utf-8",
            )

            graph = load_graph(graph_path)

        node = graph["nodes"][0]
        edge = graph["edges"][0]
        self.assertEqual(node["status"], "active")
        self.assertEqual(node["visibility"], "normal")
        self.assertEqual(node["deficiencies"], [])
        self.assertEqual(edge["status"], "active")
        self.assertEqual(edge["visibility"], "normal")

    def test_load_graph_rejects_missing_top_level_keys(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            graph_path = Path(tmpdir) / "invalid_graph.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "invalid.graph",
                        "nodes": [],
                        "edges": [],
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaises(GraphValidationError) as raised:
                load_graph(graph_path)

        self.assertIn("missing top-level keys", str(raised.exception))

    def test_load_graph_rejects_duplicate_node_ids(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            graph_path = Path(tmpdir) / "duplicate_nodes.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "duplicate.nodes",
                        "title": "Duplicate nodes",
                        "nodes": [
                            {"id": "problem.one", "kind": "problem", "title": "Problem one"},
                            {"id": "problem.one", "kind": "problem", "title": "Problem one again"},
                        ],
                        "edges": [],
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaises(GraphValidationError) as raised:
                load_graph(graph_path)

        self.assertIn("duplicate node id", str(raised.exception))

    def test_load_graph_rejects_duplicate_edge_ids(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            graph_path = Path(tmpdir) / "duplicate_edges.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "duplicate.edges",
                        "title": "Duplicate edges",
                        "nodes": [{"id": "problem.one", "kind": "problem", "title": "Problem one"}],
                        "edges": [
                            {"id": "edge.one", "from": "problem.one", "to": "problem.one", "type": "relates_to"},
                            {"id": "edge.one", "from": "problem.one", "to": "problem.one", "type": "relates_to"},
                        ],
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaises(GraphValidationError) as raised:
                load_graph(graph_path)

        self.assertIn("duplicate edge id", str(raised.exception))


class FilterSelectionTest(unittest.TestCase):
    def test_default_selection_excludes_muted_hidden_and_rejected_content(self):
        graph = load_graph(FIXTURE_PATH)

        result = select_graph(graph)

        node_ids = {node["id"] for node in result.graph["nodes"]}
        edge_ids = {edge["id"] for edge in result.graph["edges"]}
        self.assertEqual(node_ids, {"problem.root", "decision.primary"})
        self.assertEqual(edge_ids, {"edge.problem-decision"})
        self.assertIn("claim.muted", result.suppressed_node_ids)
        self.assertIn("edge.dangling", result.suppressed_edge_ids)

    def test_include_muted_restores_muted_branch_only(self):
        graph = load_graph(FIXTURE_PATH)

        result = select_graph(graph, SelectionOptions(include_muted=True))

        node_ids = {node["id"] for node in result.graph["nodes"]}
        edge_ids = {edge["id"] for edge in result.graph["edges"]}
        self.assertEqual(node_ids, {"problem.root", "decision.primary", "claim.muted"})
        self.assertEqual(edge_ids, {"edge.problem-decision", "edge.decision-muted"})

    def test_include_hidden_restores_hidden_branch_only(self):
        graph = load_graph(FIXTURE_PATH)

        result = select_graph(graph, SelectionOptions(include_hidden=True))

        node_ids = {node["id"] for node in result.graph["nodes"]}
        edge_ids = {edge["id"] for edge in result.graph["edges"]}
        self.assertEqual(node_ids, {"problem.root", "decision.primary", "risk.hidden"})
        self.assertEqual(edge_ids, {"edge.problem-decision", "edge.hidden-problem"})

    def test_all_visibility_restores_muted_and_hidden_but_not_rejected(self):
        graph = load_graph(FIXTURE_PATH)

        result = select_graph(graph, SelectionOptions(all_visibility=True))

        node_ids = {node["id"] for node in result.graph["nodes"]}
        edge_ids = {edge["id"] for edge in result.graph["edges"]}
        self.assertEqual(node_ids, {"problem.root", "decision.primary", "claim.muted", "risk.hidden"})
        self.assertEqual(
            edge_ids,
            {"edge.problem-decision", "edge.decision-muted", "edge.hidden-problem"},
        )

    def test_all_status_restores_rejected_content_without_hidden_branches(self):
        graph = load_graph(FIXTURE_PATH)

        result = select_graph(graph, SelectionOptions(all_status=True))

        node_ids = {node["id"] for node in result.graph["nodes"]}
        edge_ids = {edge["id"] for edge in result.graph["edges"]}
        self.assertEqual(node_ids, {"problem.root", "decision.primary", "option.rejected"})
        self.assertEqual(edge_ids, {"edge.problem-decision", "edge.rejected-problem"})

    def test_full_graph_selection_includes_all_visibility_and_status_content(self):
        graph = load_graph(FIXTURE_PATH)

        result = select_graph(graph, SelectionOptions(full_graph=True))

        node_ids = {node["id"] for node in result.graph["nodes"]}
        edge_ids = {edge["id"] for edge in result.graph["edges"]}
        self.assertEqual(
            node_ids,
            {"problem.root", "decision.primary", "claim.muted", "risk.hidden", "option.rejected"},
        )
        self.assertEqual(
            edge_ids,
            {
                "edge.problem-decision",
                "edge.decision-muted",
                "edge.hidden-problem",
                "edge.rejected-problem",
            },
        )
        self.assertEqual([edge["id"] for edge in result.dangling_edges], ["edge.dangling"])

    def test_focus_selection_limits_to_neighborhood(self):
        graph = load_graph(FIXTURE_PATH)

        result = select_graph(
            graph,
            SelectionOptions(full_graph=True, focus="decision.primary", depth=1),
        )

        node_ids = {node["id"] for node in result.graph["nodes"]}
        edge_ids = {edge["id"] for edge in result.graph["edges"]}
        self.assertEqual(node_ids, {"problem.root", "decision.primary", "claim.muted"})
        self.assertEqual(edge_ids, {"edge.problem-decision", "edge.decision-muted"})
        self.assertEqual(
            set(result.suppressed_node_ids),
            {"risk.hidden", "option.rejected"},
        )
        self.assertEqual(
            set(result.suppressed_edge_ids),
            {"edge.hidden-problem", "edge.rejected-problem", "edge.dangling"},
        )

    def test_focus_selection_rejects_unknown_node_id(self):
        graph = load_graph(FIXTURE_PATH)

        with self.assertRaises(ValueError) as raised:
            select_graph(graph, SelectionOptions(full_graph=True, focus="missing.node"))

        self.assertIn("focus node", str(raised.exception))

    def test_focus_selection_rejects_negative_depth(self):
        graph = load_graph(FIXTURE_PATH)

        with self.assertRaises(ValueError) as raised:
            select_graph(
                graph,
                SelectionOptions(full_graph=True, focus="decision.primary", depth=-1),
            )

        self.assertIn("depth must be zero or greater", str(raised.exception))

    def test_focus_selection_uses_default_depth_of_one_hop(self):
        graph = load_graph(FIXTURE_PATH)

        default_depth = select_graph(
            graph,
            SelectionOptions(full_graph=True, focus="decision.primary"),
        )
        wider_depth = select_graph(
            graph,
            SelectionOptions(full_graph=True, focus="decision.primary", depth=2),
        )

        default_node_ids = {node["id"] for node in default_depth.graph["nodes"]}
        wider_node_ids = {node["id"] for node in wider_depth.graph["nodes"]}
        self.assertEqual(default_node_ids, {"problem.root", "decision.primary", "claim.muted"})
        self.assertEqual(
            wider_node_ids,
            {"problem.root", "decision.primary", "claim.muted", "risk.hidden", "option.rejected"},
        )

    def test_selection_reports_dangling_edges_without_including_them(self):
        graph = load_graph(FIXTURE_PATH)

        result = select_graph(graph, SelectionOptions(full_graph=True))

        self.assertEqual([edge["id"] for edge in result.dangling_edges], ["edge.dangling"])
        self.assertNotIn("edge.dangling", {edge["id"] for edge in result.graph["edges"]})


class RendererBoundaryTest(unittest.TestCase):
    def test_build_render_graph_produces_render_ready_nodes_and_edges(self):
        graph = load_graph(FIXTURE_PATH)
        selection = select_graph(graph, SelectionOptions(full_graph=True))

        render_graph_model = build_render_graph(
            selection.graph,
            warnings=("dangling edge detected: edge.dangling",),
        )

        self.assertEqual(render_graph_model.graph_id, "sample.reasoning-map")
        self.assertEqual(render_graph_model.title, "Sample reasoning map for visualizer tests")
        self.assertEqual(render_graph_model.warnings, ("dangling edge detected: edge.dangling",))
        node_by_id = {node.raw_id: node for node in render_graph_model.nodes}
        edge_by_id = {edge.raw_id: edge for edge in render_graph_model.edges}
        self.assertEqual(node_by_id["problem.root"].label, "Root problem\n[problem]")
        self.assertIn("kind:problem", node_by_id["problem.root"].style_tokens)
        self.assertIn("deficient", node_by_id["claim.muted"].style_tokens)
        self.assertEqual(edge_by_id["edge.problem-decision"].relation, "addresses")
        self.assertIn("relation:challenges", edge_by_id["edge.hidden-problem"].style_tokens)

    def test_render_graph_emits_valid_dot_for_default_selection(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        output = render_graph(FIXTURE_PATH, output_format="dot")

        self.assertTrue(output.startswith("digraph reasoning_map {"))
        self.assertTrue(output.rstrip().endswith("}"))
        self.assertIn('label="Root problem"', output)
        self.assertIn('label="Primary decision"', output)
        self.assertIn("decision.primary", output)
        self.assertIn("problem.root", output)
        self.assertNotIn('label="addresses"', output)
        self.assertNotIn("Muted claim", output)
        self.assertNotIn("Hidden risk", output)
        self.assertNotIn("Rejected option", output)

    def test_render_graph_honors_full_graph_override(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        output = render_graph(FIXTURE_PATH, output_format="dot", full_graph=True)

        self.assertIn("Muted claim", output)
        self.assertIn("Hidden risk", output)
        self.assertIn("Rejected option", output)

    def test_render_graph_emits_mermaid_for_default_selection(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        output = render_graph(FIXTURE_PATH, output_format="mermaid")

        self.assertTrue(output.startswith("flowchart TD\n"))
        self.assertIn('problem_root["Root problem"]', output)
        self.assertIn('decision_primary{{"Primary decision"}}', output)
        self.assertIn("decision_primary -->|addresses| problem_root", output)
        self.assertNotIn("Muted claim", output)
        self.assertNotIn("Hidden risk", output)
        self.assertNotIn("Rejected option", output)

    def test_render_graph_emits_terminal_view_for_default_selection(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        output = render_graph(FIXTURE_PATH, output_format="terminal")

        self.assertIn("Graph: Sample reasoning map for visualizer tests", output)
        self.assertIn("Layer 0", output)
        self.assertIn("- problem.root [problem] Root problem", output)
        self.assertIn("Outgoing: addresses -> problem.root", output)
        self.assertNotIn("Muted claim", output)
        self.assertNotIn("Hidden risk", output)
        self.assertNotIn("Rejected option", output)

    def test_render_graph_uses_top_down_ranked_layout(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        output = render_graph(FIXTURE_PATH, output_format="dot", full_graph=True)

        self.assertIn("rankdir=TB;", output)
        self.assertIn('ranksep="1.4 equally"', output)
        self.assertIn('nodesep="0.45"', output)
        self.assertIn('subgraph "cluster_layer_0"', output)
        self.assertIn('subgraph "cluster_layer_1"', output)
        self.assertIn('subgraph "cluster_layer_2"', output)
        self.assertIn('subgraph "cluster_layer_3"', output)
        self.assertIn('"problem.root";', output)
        self.assertIn('"claim.muted";', output)
        self.assertIn('"option.rejected";', output)
        self.assertIn('"decision.primary";', output)

    def test_render_graph_compacts_labels_and_deemphasizes_secondary_edges(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        output = render_graph(FIXTURE_PATH, output_format="dot", full_graph=True)

        self.assertIn('"problem.root" [label="Root problem"', output)
        self.assertNotIn('label="Root problem\\n[problem]"', output)
        self.assertIn('"decision.primary" -> "problem.root" [color="#616161", style="solid"]', output)
        self.assertIn('"claim.muted" -> "decision.primary" [color="#616161", style="dashed", constraint="false"]', output)
        self.assertIn('"option.rejected" -> "problem.root" [label="depends_on"', output)

    def test_render_graph_applies_display_class_colors(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        output = render_graph(FIXTURE_PATH, output_format="dot", full_graph=True)

        self.assertIn('"problem.root" [label="Root problem", shape="box", color="#7c4dff"', output)
        self.assertIn('"claim.muted" [label="Muted claim", shape="ellipse", color="#8bc34a"', output)
        self.assertIn('"risk.hidden" [label="Hidden risk", shape="octagon", color="#f48fb1"', output)
        self.assertIn('"option.rejected" [label="Rejected option", shape="ellipse", color="#66bb6a"', output)
        self.assertIn('"decision.primary" [label="Primary decision", shape="hexagon", color="#66bb6a"', output)

    def test_cli_writes_dot_output_and_warns_on_dangling_edges(self):
        from tools.reasoning_map_visualizer.visualize import main

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.dot"
            stdout_buffer = io.StringIO()
            stderr_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
                exit_code = main(
                    [
                        str(FIXTURE_PATH),
                        "--format",
                        "dot",
                        "--output",
                        str(output_path),
                        "--full-graph",
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertEqual(stdout_buffer.getvalue(), "")
            self.assertTrue(output_path.exists())
            dot_output = output_path.read_text(encoding="utf-8")
            self.assertIn("Muted claim", dot_output)
            self.assertIn("Rejected option", dot_output)
            self.assertIn("dangling edge", stderr_buffer.getvalue())

    def test_cli_writes_mermaid_output(self):
        from tools.reasoning_map_visualizer.visualize import main

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.mmd"
            stdout_buffer = io.StringIO()
            stderr_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
                exit_code = main(
                    [
                        str(FIXTURE_PATH),
                        "--format",
                        "mermaid",
                        "--output",
                        str(output_path),
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertEqual(stdout_buffer.getvalue(), "")
            self.assertTrue(output_path.exists())
            self.assertIn("flowchart TD", output_path.read_text(encoding="utf-8"))
            self.assertIn("dangling edge", stderr_buffer.getvalue())

    def test_cli_prints_terminal_output(self):
        from tools.reasoning_map_visualizer.visualize import main

        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()
        with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
            exit_code = main(
                [
                    str(FIXTURE_PATH),
                    "--format",
                    "terminal",
                ]
            )

        self.assertEqual(exit_code, 0)
        self.assertIn("Graph: Sample reasoning map for visualizer tests", stdout_buffer.getvalue())
        self.assertIn("dangling edge", stderr_buffer.getvalue())

    def test_render_graph_rejects_unsupported_format(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        with self.assertRaises(ValueError) as raised:
            render_graph(FIXTURE_PATH, output_format="svg")

        self.assertIn("unsupported format", str(raised.exception))

    def test_cli_strict_mode_fails_before_writing_output(self):
        from tools.reasoning_map_visualizer.visualize import main

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.dot"
            stdout_buffer = io.StringIO()
            stderr_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
                exit_code = main(
                    [
                        str(FIXTURE_PATH),
                        "--format",
                        "dot",
                        "--output",
                        str(output_path),
                        "--full-graph",
                        "--strict",
                    ]
                )

        self.assertEqual(exit_code, 1)
        self.assertFalse(output_path.exists())
        self.assertEqual(stdout_buffer.getvalue(), "")
        self.assertIn("dangling edge", stderr_buffer.getvalue())
        self.assertIn("strict", stderr_buffer.getvalue())

    def test_render_graph_escapes_control_characters_for_dot(self):
        from tools.reasoning_map_visualizer.visualize import render_graph

        with tempfile.TemporaryDirectory() as tmpdir:
            graph_path = Path(tmpdir) / "escaped_graph.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "graph\n\"quoted\"\tname",
                        "title": "Graph\tTitle\n\"Quoted\"\rReturn",
                        "nodes": [
                            {
                                "id": "problem.\n\t\"root\"",
                                "kind": "problem",
                                "title": "Problem\n\t\"Root\"\rLine",
                                "deficiencies": ["missing\tevidence"],
                            },
                            {
                                "id": "decision.\\next",
                                "kind": "decision",
                                "title": "Decision\\Next",
                            },
                        ],
                        "edges": [
                            {
                                "id": "edge.control",
                                "from": "decision.\\next",
                                "to": "problem.\n\t\"root\"",
                                "type": "supports\n\t\"quoted\"",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            output = render_graph(graph_path, output_format="dot")

        self.assertIn('label="Graph\\tTitle\\n\\"Quoted\\"\\rReturn"', output)
        self.assertIn('"problem.\\n\\t\\"root\\""', output)
        self.assertIn('label="Problem\\n\\t\\"Root\\"\\rLine"', output)
        self.assertIn('"decision.\\\\next" -> "problem.\\n\\t\\"root\\""', output)
        self.assertIn('label="supports\\n\\t\\"quoted\\""', output)

    def test_cli_output_write_is_atomic_and_preserves_existing_file_on_replace_failure(self):
        from tools.reasoning_map_visualizer import visualize

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.dot"
            output_path.write_text("existing output\n", encoding="utf-8")
            original_content = output_path.read_text(encoding="utf-8")

            original_replace = Path.replace

            def fail_graph_output_replace(self, target):
                if self.parent == output_path.parent and self.name.startswith(f".{output_path.name}."):
                    raise OSError("replace failed")
                return original_replace(self, target)

            with mock.patch.object(visualize.Path, "replace", autospec=True, side_effect=fail_graph_output_replace):
                with self.assertRaises(OSError):
                    visualize.main(
                        [
                            str(FIXTURE_PATH),
                            "--format",
                            "dot",
                            "--output",
                            str(output_path),
                        ]
                    )

            self.assertEqual(output_path.read_text(encoding="utf-8"), original_content)
            self.assertEqual(list(output_path.parent.glob(f".{output_path.name}.*.tmp")), [])


class BatchRenderTest(unittest.TestCase):
    def test_batch_render_dry_run_reports_planned_outputs_without_writing(self):
        from tools.reasoning_map_visualizer.batch_render import main

        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = Path(tmpdir) / "graphs"
            input_dir.mkdir()
            graph_path = input_dir / "graph.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "batch.graph",
                        "title": "Batch graph",
                        "nodes": [{"id": "problem.one", "kind": "problem", "title": "Problem one"}],
                        "edges": [],
                    }
                ),
                encoding="utf-8",
            )

            stdout_buffer = io.StringIO()
            stderr_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
                exit_code = main([str(input_dir)])

        self.assertEqual(exit_code, 0)
        self.assertFalse((input_dir / "graph.dot").exists())
        self.assertIn('"dry_run": true', stdout_buffer.getvalue())
        self.assertIn('"success_count": 1', stdout_buffer.getvalue())
        self.assertEqual(stderr_buffer.getvalue(), "")

    def test_batch_render_write_mode_writes_dot_files_for_valid_graphs(self):
        from tools.reasoning_map_visualizer.batch_render import main

        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = Path(tmpdir) / "graphs"
            input_dir.mkdir()
            graph_path = input_dir / "graph.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "batch.graph",
                        "title": "Batch graph",
                        "nodes": [{"id": "problem.one", "kind": "problem", "title": "Problem one"}],
                        "edges": [],
                    }
                ),
                encoding="utf-8",
            )

            stdout_buffer = io.StringIO()
            stderr_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
                exit_code = main([str(input_dir), "--write"])

            output_path = input_dir / "graph.dot"
            output_exists = output_path.exists()
            output_text = output_path.read_text(encoding="utf-8") if output_exists else ""

        self.assertEqual(exit_code, 0)
        self.assertTrue(output_exists)
        self.assertIn("Problem one", output_text)
        self.assertIn('"written_count": 1', stdout_buffer.getvalue())
        self.assertEqual(stderr_buffer.getvalue(), "")

    def test_batch_render_write_mode_writes_mermaid_files_for_valid_graphs(self):
        from tools.reasoning_map_visualizer.batch_render import main

        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = Path(tmpdir) / "graphs"
            input_dir.mkdir()
            graph_path = input_dir / "graph.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "batch.graph",
                        "title": "Batch graph",
                        "nodes": [{"id": "problem.one", "kind": "problem", "title": "Problem one"}],
                        "edges": [],
                    }
                ),
                encoding="utf-8",
            )

            stdout_buffer = io.StringIO()
            stderr_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
                exit_code = main([str(input_dir), "--format", "mermaid", "--write"])

            output_path = input_dir / "graph.mermaid"
            output_exists = output_path.exists()
            output_text = output_path.read_text(encoding="utf-8") if output_exists else ""

        self.assertEqual(exit_code, 0)
        self.assertTrue(output_exists)
        self.assertIn("flowchart TD", output_text)
        self.assertIn('"written_count": 1', stdout_buffer.getvalue())
        self.assertEqual(stderr_buffer.getvalue(), "")

    def test_batch_render_continues_after_invalid_graph_and_exits_nonzero(self):
        from tools.reasoning_map_visualizer.batch_render import main

        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = Path(tmpdir) / "graphs"
            input_dir.mkdir()
            valid_graph_path = input_dir / "valid.json"
            valid_graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "valid.graph",
                        "title": "Valid graph",
                        "nodes": [{"id": "problem.one", "kind": "problem", "title": "Problem one"}],
                        "edges": [],
                    }
                ),
                encoding="utf-8",
            )
            invalid_graph_path = input_dir / "invalid.json"
            invalid_graph_path.write_text(
                json.dumps(
                    {
                        "graph_id": "invalid.graph",
                        "nodes": [],
                        "edges": [],
                    }
                ),
                encoding="utf-8",
            )

            stdout_buffer = io.StringIO()
            stderr_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
                exit_code = main([str(input_dir), "--write"])

            valid_output_exists = (input_dir / "valid.dot").exists()
            invalid_output_exists = (input_dir / "invalid.dot").exists()

        self.assertEqual(exit_code, 1)
        self.assertTrue(valid_output_exists)
        self.assertFalse(invalid_output_exists)
        self.assertIn('"success_count": 1', stdout_buffer.getvalue())
        self.assertIn('"failure_count": 1', stdout_buffer.getvalue())
        self.assertIn("missing top-level keys", stderr_buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
