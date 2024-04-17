from django.shortcuts import render
from SF.models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    test = Account.objects.filter(name="Abshire, Kevin & Veronica")
    return HttpResponse(test)
