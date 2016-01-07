from django.conf.urls import url
from django.views.generic import TemplateView
from atm_interface.views import BalanceView, MoneyView, ExitView, OperationView
from Atmapplication.decorators import pin_required

urlpatterns = [
    url(r'^menu/$', pin_required(TemplateView.as_view(template_name='menu.html')), name='menu'),
    url(r'^balance/$', BalanceView.as_view(), name='balance'),
    url(r'^money/$', MoneyView.as_view(), name='money'),
    url(r'^exit/$', ExitView.as_view(), name='exit'),
    url(r'^operation/$', OperationView.as_view(), name='last_operation'),
    url(r'^notenough/$', TemplateView.as_view(template_name='not_enough.html'), name='not_enough'),
]
