# Submit a payment to the Finch API

This guide shows application developers how to submit one payment safely and confirm its final outcome. The Finch OpenAPI document is authoritative for request fields and response schemas.

## How payment processing works

Finch processes payments asynchronously:

1. Submit the payment with `POST /v1/payments`.
2. Finch returns `202 Accepted` with a payment identifier.
3. Poll `GET /v1/payments/{id}` until the payment is `settled` or `failed`.

An idempotency key identifies one intended payment. Repeating the POST with the same key returns the original payment rather than creating another.

## Before you begin

Prepare:

- A Finch bearer token.
- A request body conforming to the OpenAPI schema.
- An idempotency key that remains stable for this payment.

Do not reuse that key for a different intended payment: Finch would return the payment originally associated with it.

## Submit the payment

Send the request defined by the OpenAPI document:

```http
POST /v1/payments HTTP/1.1
Authorization: Bearer <token>
Idempotency-Key: <key-for-this-payment>

<request body defined by the OpenAPI schema>
```

A successful request returns:

```http
HTTP/1.1 202 Accepted
```

The response contains the payment identifier. Retain both the identifier and idempotency key so the application can track the payment and safely repeat the submission if necessary.

A `202 Accepted` response means processing has started; it does not mean the payment has settled.

## Check the payment outcome

Use the identifier from the submission response:

```http
GET /v1/payments/<payment-id> HTTP/1.1
Authorization: Bearer <token>
```

Inspect the response status:

- `settled` — processing completed successfully.
- `failed` — processing completed unsuccessfully.
- Any other documented status — processing is not yet terminal; poll again.

The OpenAPI document defines the complete response shape and any additional status fields.

## Retry safely

For a retried POST, send the identical payment request with the same idempotency key. Finch returns the original payment instead of creating a duplicate.

Apply this response policy:

| Response | Action |
|---|---|
| `202 Accepted` | Record the payment identifier and begin polling. |
| `429` | Retry with exponential backoff. |
| `503` | Retry with exponential backoff. |
| Other `4xx` | Do not retry automatically; correct the request or credentials first. |

The repository evidence does not define backoff timing or a maximum attempt count. Choose those limits as part of the application's retry policy rather than assuming Finch-specific defaults.

If the connection fails before the application receives a response, repeating the POST with the same idempotency key avoids intentionally creating a second payment.

## Verify the integration

A production integration is complete when it can demonstrate that:

1. A valid POST returns `202 Accepted` and a payment identifier.
2. Repeating that POST with the same idempotency key returns the original payment.
3. Polling the returned identifier eventually observes either `settled` or `failed`.
4. Automatic retries are limited to `429` and `503` responses and use exponential backoff.
5. Other `4xx` responses stop automatic retry and surface the error for correction.
