from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Trip
from ..loginreg.models import User
from django.contrib import messages
from datetime import datetime

def index(request):
    user_id = request.session["id"]
    context = {
        "trips":Trip.objects.all()[:5],
        "me": Trip.objects.filter(user_id=user_id),
        "me2": Trip.objects.all().filter(travelers=user_id),
        "notme": Trip.objects.all().exclude(travelers=user_id).exclude(user=user_id)
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
    if request.POST["trip_begin"] and request.POST["trip_end"]:
        user = User.objects.get(id=request.session['id'])
        description = request.POST["description"]
        trip_begin = datetime.strptime(request.POST["trip_begin"], '%Y-%m-%d')
        trip_end = datetime.strptime(request.POST["trip_end"], '%Y-%m-%d')
        destination=request.POST["destination"]
        print trip_begin

        if len(description) >1 and len(description) >1 and trip_begin > datetime.now() and trip_end > trip_begin:
            trip = Trip.objects.create(description=description, trip_begin=trip_begin, trip_end=trip_end, destination=destination, user=user)
            return redirect(reverse('pythonbeltapp:show', kwargs={"trip_id":trip.id}))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        return render(request, 'pythonbeltapp/add.html')

def update(request, trip_id):
    userid = User.objects.get(id=request.session['id'])
    selected_trip = Trip.objects.get(id=trip_id)
    selected_trip.travelers.add(userid)
    selected_trip.save()
    return redirect(reverse('pythonbeltapp:show', kwargs={"trip_id":selected_trip.id}))
