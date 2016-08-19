from django.shortcuts import render, HttpResponse, redirect
# from .models import People
from ..loginreg.models import User

def index(request):
    context = { "somekey":"somevalue" }
    return render(request, 'pythonbeltapp/index.html', context)
