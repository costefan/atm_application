from django.shortcuts import render, redirect


def card_required(view_func):
    def wrapped_func(request, *args, **kwargs):
        if request.session['card_id']:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/error')
    return wrapped_func


def pin_required(view_func):
    def wrapped_func(request, *args, **kwargs):
        if request.session['pin_required']:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/error')
    return wrapped_func
