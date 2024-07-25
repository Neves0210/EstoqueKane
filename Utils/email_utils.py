import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

def send_admin_email(username):
    # Configuração do servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv('EMAIL_USER')
    sender_password = os.getenv('EMAIL_PASSWORD')
    
    # Mensagem de email
    message = MIMEText(f"Novo registro de usuário pendente: {username}")
    message['Subject'] = "Aprovação de Novo Usuário"
    message['From'] = sender_email
    message['To'] = "ga.barros0210@outlook.com"  # Coloque o email do administrador

    # Envio do email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
