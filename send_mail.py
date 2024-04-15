import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    # Datos del correo electrónico
    sender_email = "pruebacomprasinternas@gmail.com"
    receiver_email = "sistemas@farmaciasdrahorro.com.ar"
    password = "znxp vdfv isiu mbil"

    # Crear un mensaje
    message = MIMEText(body, "plain")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Conexión al servidor SMTP de Gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Correo electrónico enviado con éxito.")