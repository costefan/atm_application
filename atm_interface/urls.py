from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from atm_interface.views import BalanceView

urlpatterns = [
    url(r'^menu/$', TemplateView.as_view(template_name='menu.html'), name='menu'),
    url(r'^balance/$', BalanceView.as_view(), name='balance'),
    url(r'^money/$', BalanceView.as_view(), name='money'),
    url(r'^operation/$', BalanceView.as_view(), name='last_operation'),
]
