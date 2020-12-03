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
    regionlistitems = Region.objects.filter(country_id=id)
    regionlist = []
    regionlistchildren = {}
    for r in regionlistitems:
        if r.pid:
            if r.pid not in regionlistchildren:
                regionlistchildren[r.pid] = []
            regionlistchildren[r.pid].append(r)
        else:
            regionlist.append(r)
    context = {
        'id': id,
        'regionlist': regionlist,
        'regionlistchildren': regionlistchildren
    }
    return render(request, 'geo/add_region.html', context)


def create_region(request, id):
    if request.method == 'POST':
        c = Country.objects.get(pk=id)
        r = Region()
        r.country_id = id
        r.name = request.POST['name']
        r.save()
    return redirect('/geo/country/'+str(id)+'/add_region')


def region_delete(request, id):
    r = Region.objects.get(pk=id)
    cid = r.country_id
    r.delete()
    return redirect('/geo/country/'+str(cid)+'/add_region')


def add_child_region(request, id):
    regionlist = Region.objects.filter(pid=id)
    context = {
        'id': id,
        'regionlist': regionlist
    }
    return render(request, 'geo/add_child_region.html', context)


def create_child_region(request, id):
    if request.method == 'POST':
        r2 = Region.objects.get(pk=id)
        r = Region()
        r.pid = r2
        r.country_id = r2.country_id
        r.name = request.POST['name']
        r.save()
    return redirect('/geo/country/' + str(id) + '/add_region')