from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from time import sleep
from .task import *
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from docx2pdf import convert
from celery.result import AsyncResult


# Create your views here.

def index(request):
    # sleep(10)
    sleepy.delay(20)
    return HttpResponse("Hellow World")

# def send_mail_without_celery(request):
#     print("Email is good")
#     send_mail("CELERY WORKED YEAH",
#     "CELERY IS COOL",
#     "331rahul@gmail.com",
#     ["rahulsayon92@gmail.com"])
#     return HttpResponse("Hello Rahul")



def send_mail_without_celery(request):
    send_email_task.delay()
    return HttpResponse("Hello Rahul")


def uploadfile(request):
    if request.method == "POST":
        print("yesssssss")
        fs = FileSystemStorage()
        myfile = request.FILES["file"]
        filename = fs.save(myfile.name , myfile)
        uploaded_file_url = fs.url(filename)
        data = convert_doc_to_pdf.delay(myfile.name)
        return HttpResponseRedirect(data.task_id)
    return render(request,"celeryshow/index.html")



def check_status(request , task_id):
    res = AsyncResult(task_id)
    # print(res.ready())
    context = {'task_status': res.ready()}
    return render(request , 'celeryshow/progress.html' ,context)
    
    