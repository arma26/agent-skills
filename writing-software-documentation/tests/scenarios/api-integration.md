# Scenario: API integration

Document how an application submits a payment to the Finch API.

Repository evidence:

- Clients send `POST /v1/payments` with a bearer token and an `Idempotency-Key` header.
- A successful request returns `202 Accepted` and a payment identifier; processing continues asynchronously.
- Clients inspect `GET /v1/payments/{id}` until the status is `settled` or `failed`.
- Repeating a POST with the same idempotency key returns the original payment instead of creating another.
- `429` and `503` responses may be retried with exponential backoff; other `4xx` responses must not be retried automatically.
- The OpenAPI document is authoritative for fields and response schemas.

Primary reader: an application developer making their first production integration.
