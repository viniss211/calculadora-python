import smtplib
import os

EMAIL = os.environ.get("EMAIL_USERNAME")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
TO = os.environ.get("EMAIL_TO")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL, PASSWORD)
    subject = "Relatorio do Pipeline"
    body = "Pipeline executado com sucesso!" #
    msg = f"Subject: {subject}\n\n{body}"
    smtp.sendmail(EMAIL, TO, msg)
