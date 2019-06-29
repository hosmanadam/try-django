from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    context: dict = {
        'phone': '+12 345 6789',
        'email': 'mail@gmail.com',
        'address': '1 Best Street',
        'stuff': [123, 456, 789]
    }
    return render(request, 'contact.html', context)


def injected_view(request, *args, **kwargs):
    return HttpResponse(f'<h1>Injected: {args[0]}</h1>')
