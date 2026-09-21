# Project Type Matrix

## Goal

Adjust public-facing expectations by project type while keeping the same example-first, low-friction posture.

## Library

Show:

- install command
- smallest import-and-use example
- expected output or effect
- one slightly richer example

Watch for:

- architecture explanation before usage
- examples that require too much scaffolding
- unclear public API boundaries

## CLI

Show:

- install or run command
- one trivial invocation
- expected output
- one realistic invocation

Watch for:

- flags described without example commands
- no visible output examples
- workflow wrappers that hide ordinary CLI behavior

## Service Or API

Show:

- exact startup commands
- minimal dependency story
- one request-response path
- required env vars only

Watch for:

- local boot path omitted
- stateful behavior not explained
- `.env` shape implied rather than shown

## Web App

Show:

- install and run commands
- first route or screen
- minimal verification path
- clear layout between frontend, backend, and assets when relevant

Watch for:

- screenshots substituting for runnable instructions
- no obvious local run path
- unclear feature location in the repo

## Research Or Exploratory Project

Show:

- explicit status
- reproducible path
- exact input expectations
- narrow claims

Watch for:

- prototype residue presented as maintained product surface
- claims that exceed reproducibility
- experiment artifacts mixed with durable project code
