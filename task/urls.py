from django.contrib import admin
from django.conf.urls import url
from task import views
urlpatterns = [
    url(r'^add_subscriber',views.Add_Subscribers.as_view()),
    url(r'^remove_subscriber',views.Remove_Subscribers.as_view()),
]
