from django.core.mail import send_mail

from test_task.celery import app
from .models import Contact
from .service import send


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать вам письма каждые 5 минут',
            'forgjangoproject@gmail.com',
            [contact.email],
            fail_silently=False
        )
