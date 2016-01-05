from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from atm_interface.models import Card
from django.utils import timezone





class BalanceView(TemplateView):
    template_name = 'balance.html'

    def get(self, request, *args, **kwargs):
        card = Card.objects.get(pk=request.session['card_id'])
        now = timezone.now()
        return render(request, self.template_name, {'card': card, 'time': now})
