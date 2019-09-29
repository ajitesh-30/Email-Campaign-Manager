from django.db import models
from django import template
from datetime import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import Context

class Subscribers(models.Model):
    email = models.EmailField(max_length=70,unique=True)
    first_name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)


class CampaignManager(models.Model):
    preview_text = models.TextField(null=True)
    article_url = models.TextField(null=True)
    html_template = models.TextField(blank=True, null=True)
    plain_text = models.TextField(blank=True, null=True)
    published_date  = models.DateTimeField(default=datetime.now())
    template_key = models.CharField(max_length=255, unique=True)