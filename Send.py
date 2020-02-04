from flask import Flask
from flask_mail import Mail, Message
import os
app = Flask(__name__)
################## v1 ########

class Config:
    """
       Класс настроек приложения Flask
    """
    # Включаем отладку приложения Flask
    DEBUG = True
    # Настройки расширения Flask-Mail
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    # Используем переменные окружения для инициализации логина и пароля
    MAIL_USERNAME = 'timoshaborisov@yandex.ru'
    MAIL_PASSWORD = ''

#################### v2 ##########################
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}
###################################

app.config.from_object(Config)
#v2 app.config.update(mail_settings)
mail = Mail(app)


if __name__ == '__main__':
    with app.app_context():
        msg = Message(subject="Hello",
                      sender="timoshaborisov@yandex.ru",
                      recipients=["tbs999borisov@gmail.com"], # replace with your email for testing
                      body="This is a test email I sent with Python!")
        mail.send(msg)

app.run(debug=True)