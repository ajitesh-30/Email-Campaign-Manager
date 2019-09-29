import logging
from django.core.mail import EmailMessage
from django.urls import reverse
from .models import CampaignManager,Subscribers
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from CampaignManager.celery import app
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.template.loader import render_to_string
 
@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="send_email",
    ignore_result=True
)
def send_campaign_email():
	template = 'base.html'
	from_email = 'ajiteshs10@gmail.com'
	plain = 'This is a test mail'
	html = render_to_string('base.html',{
		'subject' : 'This is the mail subject',
		'preview_text' : 'This is the preview_text',
		'article_url' : 'https//articleurl.co'
	})
	subsribers = Subscribers.objects.all()
	for mail in subscribers:
		send_mail('email_title', plain, from_email, 
                ['ajiteshs10@gmail.com'],  html_message=html,
                fail_silently=False
       )
