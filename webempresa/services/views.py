from django.shortcuts import render
from .models import Service


def services (request):
    services = Service.objects.all() #Esto permite que se accedan a los servicios de la bd
    return render(request, 'services/services.html',{'services':services})
