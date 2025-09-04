from fastapi import APIRouter, HTTPException
from app.models.email_models import EmailRequest
import smtplib

router = APIRouter()

@router.post("/email/send")
def send_email(req: EmailRequest):
    try:
        smtp_server = "localhost"
        smtp_port = 1025  # use a local debugging SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            message = f"Subject: {req.subject}\n\n{req.body}"
            server.sendmail("you@example.com", req.recipient, message)
        return {"status": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
