from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CampaignManager.settings')
 
app = Celery('CampaignManager')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule={
	'send-mails-everyday': {
        'task': 'task.tasks.send_campaign_email',
        'schedule': crontab(minute=0,hour=0),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}