from django.shortcuts import render, redirect


def card_required(view_func):
    def wrapped_func(request, *args, **kwargs):
        try:
            request.session['card_id']
        except KeyError:
            return redirect('/error')
        return view_func(request, *args, **kwargs)

    return wrapped_func


def pin_required(view_func):
    def wrapped_func(request, *args, **kwargs):
        try:
            request.session['pin_required']
        except KeyError:
            return redirect('/error')
        return view_func(request, *args, **kwargs)

    return wrapped_func
