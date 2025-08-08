from fastapi import FastAPI, Request, HTTPException
import imaplib
import email
import datetime  # 🔧 Required for timestamp

app = FastAPI()

@app.post("/append-to-sent")
async def append_to_sent(request: Request):
    try:
        data = await request.json()
        
        # Connect to IMAP
        mail = imaplib.IMAP4_SSL(data["imapHost"], int(data["imapPort"]))
        mail.login(data["imapUsername"], data["imapPassword"])

        # Build message
        msg = email.message_from_string(data["rawMessage"])

        # Append to Sent with proper timestamp
        mail.append('"Sent"', '', imaplib.Time2Internaldate(datetime.datetime.now()), msg.as_bytes())
        
        mail.logout()
        return {"status": "success"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
