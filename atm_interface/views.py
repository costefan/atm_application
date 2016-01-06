from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from atm_interface.models import Card, Operation
from django.utils import timezone
from django.utils.decorators import method_decorator
from Atmapplication.decorators import pin_required


@method_decorator(pin_required, name='get')
class BalanceView(TemplateView):
    """
    Gives information about balance of the card
    """
    template_name = 'balance.html'

    def get(self, request, *args, **kwargs):
        card = Card.objects.get(pk=request.session['card_id'])
        now = timezone.now()
        Operation.objects.create(card=card,
                                 time=now,
                                 code=1)
        return render(request, self.template_name, {'card': card, 'time': now})


@method_decorator(pin_required, name='get')
class MoneyView(TemplateView):
    """

    """
    template_name = 'money.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        card = Card.objects.get(pk=request.session['card_id'])
        if request.POST.get('money') is not None:
            if int(request.POST.get('money')) <= card.cash:
                now = timezone.now()
                old_val = card.cash
                Card.objects.filter(pk=card.id).update(cash=old_val - int(request.POST.get('money')))
                Operation.objects.create(card=card,
                                         time=now,
                                         code=2,
                                         cash=int(request.POST.get('money')))
                return redirect('/interface/operation')
            return redirect('/interface/notenough')
        return render(request, self.template_name, {'message': 'Please,enter number'})


@method_decorator(pin_required, name='get')
class OperationView(TemplateView):
    """

    """
    template_name = 'last_operation.html'

    def get(self, request, *args, **kwargs):
        last_operation = Operation.objects.last()
        return render(request, self.template_name, {'operation': last_operation})
