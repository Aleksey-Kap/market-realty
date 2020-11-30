from django.shortcuts import render, redirect
from flat.models import Country, Region
from .forms import CountryForm

# Create your views here.


def index(request):

    countrylist = Country.objects.all()
    form = CountryForm()
    context = {
        'countrylist': countrylist,
        'form': form
        }
    return render(request, 'geo/index.html', context)


def country_delete(request, id):
    Country.objects.get(pk=id).delete()
    return redirect('/geo')


def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/geo/')


def add_region(request, id):
    regionlist = Region.objects.filter(country_id=id)
    context = {
        'id': id,
        'regionlist': regionlist
    }
    return render(request, 'geo/add_region.html', context)


def create_region(request, id):
    if request.method == 'POST':
        c = Country.objects.get(pk=id)
        r = Region()
        r.сountry_id = id
        r.name = request.POST['name']
        r.save()
    return redirect('/country/'+id+'/add_region')


