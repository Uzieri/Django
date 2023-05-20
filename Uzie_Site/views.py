from django.http import HttpResponse
from django.shortcuts import render
from .models import Vehicles
from django.http import HttpResponseRedirect
from django.http import Http404



def Uzie_Site(request):
   data = Vehicles.objects.all()
   return render(request, 'Uzie_Site/Uzie_Site.html', {'Uzie_Site':data})

def home(request):

    return HttpResponse("Vehicle Categories")

def detail(request, id):
    data = Vehicles.objects.get(pk=id)
    return render (request, 'Uzie_Site/detail.html', {'Vehicle' : data} )
def add(request):
    Name = request.POST.get('Name')
    year = request.POST.get('year')

    if Name and year:
        Vehicle = Vehicles(Name = Name, year = year)
        Vehicle.save()
        return HttpResponseRedirect('/Uzie_Site')
    return render(request, 'Uzie_Site/add.html')
def delete(request, id):
    try:
       Vehicle = Vehicles.objects.get(pk = id)
    except:
          raise Http404('Vehicle does not exist')
    Vehicle.delete()
    return HttpResponseRedirect('/Uzie_Site')