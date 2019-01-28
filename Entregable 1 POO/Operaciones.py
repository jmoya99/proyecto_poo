import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
    Correo: saan.unal@gmail.com
    Contraseña: SAAN12345
"""

class Operaciones:
    
    @staticmethod
    def enviar_correo_electronico(correo_enviar,asunto,cuerpo):
        server = smtplib.SMTP(host='smtp-relay.gmail.com',port=587)
        msg = MIMEMultipart()
        password = "SAAN12345"
        msg['From'] = "saan.unal@gmail.com"
        msg['To'] = correo_enviar
        msg['Subject'] = asunto
        msg.attach(MIMEText(cuerpo,'plain'))
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit()
        return "Correo enviado"
