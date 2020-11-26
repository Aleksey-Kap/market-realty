from django.shortcuts import render, redirect
from flat.models import Country

# Create your views here.


def index(request):
    countrylist = Country.objects.all()
    context = {
        'countrylist': countrylist
    }
    return render(request, 'geo/index.html', context)


def country_delete(request, id):
    Country.objects.get(pk=id).delete()
    return redirect('/geo')