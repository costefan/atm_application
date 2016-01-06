from django.conf.urls import url
from django.views.generic import TemplateView
from atm_interface.views import BalanceView, MoneyView

urlpatterns = [
    url(r'^menu/$', TemplateView.as_view(template_name='menu.html'), name='menu'),
    url(r'^balance/$', BalanceView.as_view(), name='balance'),
    url(r'^money/$', MoneyView.as_view(), name='money'),
    url(r'^operation/$', TemplateView.as_view(template_name='last_operation.html'), name='last_operation'),
    url(r'^notenough/$', TemplateView.as_view(template_name='not_enough.html'), name='not_enough'),
]
