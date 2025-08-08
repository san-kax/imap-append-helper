from fastapi import FastAPI, Request, HTTPException
import imaplib
import email
from datetime import datetime, timezone

app = FastAPI()

@app.post("/append-to-sent")
async def append_to_sent(request: Request):
    try:
        data = await request.json()

        mail = imaplib.IMAP4_SSL(data["imapHost"], int(data["imapPort"]))
        mail.login(data["imapUsername"], data["imapPassword"])

        msg = email.message_from_string(data["rawMessage"])
        now = datetime.now(timezone.utc)  # timezone-aware datetime
        mail.append('"Sent"', '', imaplib.Time2Internaldate(now), msg.as_bytes())

        mail.logout()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
