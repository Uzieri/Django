from django.http import HttpResponse
from django.shortcuts import render

data = {
'Uzie_Site':[
    {
       'Engine_No': 234,
        'Name': 'Isuzu',
        'Year': 2017
    },
    {
        'Engine_No': 134,
        'Name': 'Toyota',
        'Year': 2019
    },
    {
        'Engine_No': 235,
        'Name': 'Hino',
        'Year': 2020
    }
            ]
}

def Uzie_Site(request):

    return render(request, 'Uzie_Site/Uzie_Site.html', data)
def home(request):

    return HttpResponse("Vehicle Categories")
