from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^menu/$', TemplateView.as_view(template_name='menu.html'), name='menu'),

]
