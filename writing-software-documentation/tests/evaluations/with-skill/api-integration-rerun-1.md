# Submit a payment to the Finch API

This guide shows application developers how to submit one payment safely and confirm its final outcome.

A successful submission does not mean the payment has settled. Finch accepts the payment asynchronously:

1. Submit the payment with `POST /v1/payments`.
2. Receive `202 Accepted` and a payment identifier.
3. Inspect `GET /v1/payments/{id}` until the payment is `settled` or `failed`.

The Finch OpenAPI document is authoritative for request fields and response schemas.

## Submit the payment

Before sending the request, prepare:

- A bearer token.
- A request body that conforms to the OpenAPI schema.
- An idempotency key for this logical payment.

Send the payment:

```http
POST /v1/payments HTTP/1.1
Authorization: Bearer <token>
Idempotency-Key: <idempotency-key>
Content-Type: application/json

<request body defined by the OpenAPI document>
```

A successful request returns:

```http
HTTP/1.1 202 Accepted

<response containing the payment identifier>
```

Extract the identifier using the response schema in the OpenAPI document. Do not treat `202 Accepted` as confirmation that the payment has settled; it only confirms that asynchronous processing has begun.

## Preserve the idempotency key

Keep the idempotency key associated with the payment until the submission outcome is known. If the response is lost or the request must be retried, repeat the POST with the same request and the same key:

```http
POST /v1/payments HTTP/1.1
Authorization: Bearer <token>
Idempotency-Key: <same-idempotency-key>
Content-Type: application/json

<same request body>
```

Finch returns the original payment instead of creating another one.

As integration guidance, use a different idempotency key for each distinct logical payment. Replacing the key during recovery removes the documented duplicate-payment protection.

## Inspect the payment status

Use the payment identifier from the accepted response:

```http
GET /v1/payments/<payment-id> HTTP/1.1
```

Read the status from the response according to the OpenAPI schema:

- `settled`: processing completed successfully; stop polling.
- `failed`: processing ended unsuccessfully; stop polling.
- Any other documented status: processing has not reached either terminal outcome; inspect the payment again later.

The available evidence does not define a polling interval or a recovery procedure for a `failed` payment. Do not invent either behavior in the integration; follow additional Finch guidance where available.

## Handle retryable responses

A `429` or `503` response may be retried with exponential backoff.

For a retried submission, preserve the original idempotency key so the retry resolves to the original payment. Apply the same backoff policy when a status request receives either retryable response.

Other `4xx` responses must not be retried automatically. Stop the retry loop and handle the response using the error schema in the OpenAPI document.

The available evidence does not establish retry behavior for other response classes, backoff timing, or retry limits. Define those policies only from additional authoritative Finch documentation.
