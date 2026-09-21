# Submit a payment

Finch processes payments asynchronously. Your application submits a payment, stores the returned payment identifier, and checks the payment until it reaches a terminal status.

For exact request fields and response schemas, use the OpenAPI document as the authoritative reference.

## Before you begin

Prepare:

- A Finch API bearer token
- A unique idempotency key for the payment
- A JSON request body that conforms to the OpenAPI schema

Keep bearer tokens secret. Do not expose them in client-side code, logs, or source control.

## 1. Submit the payment

Send a `POST` request to `/v1/payments` with the bearer token and an `Idempotency-Key` header:

```bash
curl --request POST \
  --url "${FINCH_BASE_URL}/v1/payments" \
  --header "Authorization: Bearer ${FINCH_API_TOKEN}" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
  --data @payment.json
```

A successful request returns `202 Accepted` and a payment identifier. The payment is accepted for processing, but it is not yet settled.

Persist the payment identifier so your application can inspect the payment later.

## 2. Check the payment status

Request the payment by its identifier:

```bash
curl --request GET \
  --url "${FINCH_BASE_URL}/v1/payments/${PAYMENT_ID}" \
  --header "Authorization: Bearer ${FINCH_API_TOKEN}"
```

Continue checking until the response reports one of these terminal statuses:

- `settled`: processing completed successfully
- `failed`: processing did not complete successfully

Treat other statuses as non-terminal. Wait before checking again rather than polling continuously.

## Prevent duplicate payments

Generate one idempotency key for each logical payment and reuse that key whenever you retry its submission.

If a connection fails or the response is lost, submit the same request again with the same idempotency key. Finch returns the original payment instead of creating another.

Do not generate a new key merely because the first request timed out. A new key represents a new logical payment and can result in a duplicate charge.

Store the following values together until the payment reaches a terminal status:

- Your internal payment reference
- The idempotency key
- The Finch payment identifier, once received
- The latest known payment status

## Retry safely

Automatically retry only these responses:

- `429 Too Many Requests`
- `503 Service Unavailable`

Use exponential backoff between attempts and cap both the delay and total number of attempts. Add jitter when many workers may retry concurrently.

For example:

```text
delay = initial_delay

for each attempt:
    response = send_request()

    if response is successful:
        return response

    if response status is not 429 or 503:
        return error without retrying

    wait for delay plus jitter
    delay = min(delay * 2, maximum_delay)

return retry_exhausted
```

Do not automatically retry other `4xx` responses. They indicate a request problem that should be corrected before resubmission.

Every retry of `POST /v1/payments` must use the original idempotency key.

## Production checklist

Before enabling payments in production, verify that your application:

- Sends bearer tokens only over HTTPS
- Uses a unique idempotency key for every logical payment
- Reuses that key for retries of the same payment
- Persists the returned payment identifier
- Handles `202 Accepted` as asynchronous acceptance, not settlement
- Checks status until it becomes `settled` or `failed`
- Retries only `429` and `503` responses automatically
- Uses bounded exponential backoff with jitter
- Validates request and response fields against the OpenAPI document
