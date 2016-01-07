from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from atm_interface.models import Card, Operation
import datetime
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
        now = datetime.datetime.now()
        Operation.objects.create(card=card,
                                 time=now,
                                 code=1)
        return render(request, self.template_name, {'card': card, 'time': now})


@method_decorator(pin_required, name='get')
class MoneyView(TemplateView):
    """
    Gives user ability to get his money

    if all is ok - redirect to operation
    """
    template_name = 'money.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        card = Card.objects.get(pk=request.session['card_id'])
        if request.POST.get('money') is not None:
            if int(request.POST.get('money')) <= card.cash:
                now = datetime.datetime.now()
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
    Gives information about last operation
    """
    template_name = 'last_operation.html'

    def get(self, request, *args, **kwargs):
        last_operation = Operation.objects.last()
        card = last_operation.card
        return render(request, self.template_name, {'operation': last_operation,
                                                    'card': card})


@method_decorator(pin_required, name='post')
class ExitView(TemplateView):
    """

    """
    template_name = 'login.html'
    def post(self, request):
        request.session.pop('pin_required')
        request.session.pop('card_id')
        return redirect('/')
