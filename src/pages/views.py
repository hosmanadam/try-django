from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(request)
    return HttpResponse(f'<h1>Home page</h1>')


def contact_view(request, *args, **kwargs):
    return HttpResponse(f'<h1>Contact page</h1>')


def injected_view(request, *args, **kwargs):
    return HttpResponse(f'<h1>Injected: {args[0]}</h1>')
