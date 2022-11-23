from django.shortcuts import render
from django.http import HttpResponse
from . models import spot, teams

def index(request):
    obj = spot.objects.all()
    obj1 = teams.objects.all()
    return render(request, 'index.html', {'place':obj, 'team':obj1})


    
# Create your views here.
