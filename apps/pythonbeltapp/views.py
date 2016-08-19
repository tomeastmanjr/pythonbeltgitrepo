from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Trip
from ..loginreg.models import User
from django.contrib import messages

def index(request):
    user_id = request.session["id"]
    context = {
        "trips":Trip.objects.all()
    }
    return render(request, 'pythonbeltapp/index.html', context)

def show(request, trip_id):
    context = {
        "trip": Trip.objects.get(id=trip_id),
        "users": User.objects.all()
    }
    return render(request, 'pythonbeltapp/destination.html', context)

def add(request):
    return render(request, 'pythonbeltapp/add.html')

def create(request):
    user = User.objects.get(id=request.session['id'])
    description = request.POST["description"]
    trip_begin=request.POST["trip_begin"]
    trip_end=request.POST["trip_end"]
    destination=request.POST["destination"]

    if len(description) >1 and len(description) >1:
        trip = Trip.objects.create(description=description, trip_begin=trip_begin, trip_end=trip_end, destination=destination, user=user)
        return redirect(reverse('pythonbeltapp:show', kwargs={"trip_id":trip.id}))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        return render(request, 'pythonbeltapp/add.html')

def update(request, trip_id):
    user = User.objects.get(id=request.session['id'])
    trip1 = Trip.objects.get(id=trip_id)
    trip1.travelers.add(user)
    trip1.save()
    return redirect(reverse('pythonbeltapp:show', kwargs={"trip_id":trip1.id}))
