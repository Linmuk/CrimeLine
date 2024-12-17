from django.shortcuts import render
from .models import Incident
# Create your views here.



def dashboard(request):
    incidents = Incident.objects.all()
    return render(request, 'police/dashboard.html', {'incidents': incidents})
