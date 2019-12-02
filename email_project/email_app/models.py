from django.db import models


class Email(models.Model):
    email_ids = models.CharField(max_length=255)
    cc = models.CharField(max_length=255)
    bcc = models.CharField(max_length=255)
    subject = models.CharField(max_length=1024)
    body = models.TextField(max_length=1024)
    send_time = models.DateField(auto_now_add=True)
    document = models.FileField(upload_to='documents/')

