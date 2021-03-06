from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from Atmapplication.decorators import card_required
from .forms import CardNumberForm
from atm_interface.models import Card


class LoginView(TemplateView):
    """
    User can login by his card number

    When gives right card number - redirected to PinView
    """
    template_name = 'login.html'
    form_class = CardNumberForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            number = ''.join(form.cleaned_data['number'].split('-'))
            try:
                card = Card.objects.get(number=number)
            except Card.DoesNotExist:
                return render(request, self.template_name, {'form': form, 'message': 'Invalid card number'})

            if not card.blocked:
                request.session['card_id'] = card.id
                request.session['incorrect_times'] = 0
                return redirect('/pin')
            return redirect('/blocked')

        return render(request, self.template_name, {'form': form, 'message': 'Invalid card number'})


@method_decorator(card_required, name='get')
class PinView(TemplateView):
    """
    Check pin of the card

    When given right - redirected to the MenuView
    If he gave incorrect pin 4 times - his card will be blocked
    """
    template_name = 'pin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        card = Card.objects.get(pk=request.session['card_id'])
        request.session['incorrect_times'] += 1

        while request.session['incorrect_times'] < 4:
            if request.POST.get('password') == card.pin:
                request.session['pin_required'] = True
                request.session.pop('incorrect_times')
                request.session.modified = True
                return redirect('/interface/menu/')
            else:
                return render(request, self.template_name, {'message': 'Incorrect pin, please try again'})
        else:
            Card.objects.filter(pk=card.id).update(blocked=True)
            return redirect('/blocked')
