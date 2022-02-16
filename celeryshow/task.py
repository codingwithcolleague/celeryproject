from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from docx2pdf import convert

@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    send_mail("CELERY WORKED YEAH",
    "CELERY IS COOL",
    "331rahul@gmail.com",
    ["rahulsayon92@gmail.com"])
    return None


@shared_task
def convert_doc_to_pdf(myfile):
    sleep(10)
    convert('static/' + myfile)
    return None