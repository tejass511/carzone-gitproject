from django.shortcuts import render
from .models import Teams

# Create your views here.
def home(request):
    teamss=Teams.objects.all()
    data={
        'teamss':teamss,
    }
    return render(request, 'pages/home.html',data)

def about(request):
    teamss=Teams.objects.all()
    data={
        'teamss':teamss
    }
    return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
