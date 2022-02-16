
from django.urls import path
from .views import index,send_mail_without_celery,uploadfile,check_status


urlpatterns = [
    path('' , index , name="index"),
    path('sendemail/' , send_mail_without_celery , name="sendemail"),
    path("uploadfile/" , uploadfile , name="showproject"),
    path('uploadfile/<task_id>/' , check_status , name="check_status"),

    ]