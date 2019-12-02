Create an application in python with Django which will send an email to a particular user using basic UI. This portal should be like email service and should include email Id/ids, subject, and body, cc, bcc. Also, there should be provision to upload CSV file with a list of email Ids to send an email. Use the ELK stack for log management.

After every 30 mins, an email will be sent to admin with all the email statistics of a day i.e; total email sent and timestamp of each email.  



1.Readme.MD 
     -> This file should contain all application configuration information.
     -> All steps to run the application.
2.> requirement.txt


Django project + api - 1 hour
ELK setup if done in Kubernetes - 1 hour
Celery task queue / airflow for sending 30 mins of summary emails - 2 hours, otherwise 1 hour if Django management command with a cronjob is used instead of a job queue
Testing - 1 hour
Deployment to Kubernetes for ELK - 1 hour

# Getting Started
```bash
django-admin startproject email_service .

python3 manage.py startapp email_app

python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000

python3 manage.py createsuperuser
```
