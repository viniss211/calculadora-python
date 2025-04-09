import smtplib
import os

EMAIL = os.environ.get("EMAIL_SENDER")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
TO = os.environ.get("EMAIL_RECEIVER")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL, PASSWORD)
    subject = "Relatório do Pipeline"
    body = "Pipeline executado com sucesso!"
    msg = f"Subject: {subject}\n\n{body}"
    smtp.sendmail(EMAIL, TO, msg)
