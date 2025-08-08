# IMAP Append-to-Sent Helper

This FastAPI app allows appending a raw RFC822 email message to the "Sent" folder of any mailbox via IMAP.

## Endpoint

### `POST /append-to-sent`

**Payload:**
```json
{
  "imapHost": "imap.server.com",
  "imapPort": 993,
  "imapUsername": "user@example.com",
  "imapPassword": "password",
  "rawMessage": "RFC822 formatted email string"
}
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 10000
```

## Deploy (e.g., on Render)

- Use Python 3.11+
- Start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
