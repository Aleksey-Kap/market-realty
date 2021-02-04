from django.shortcuts import render, redirect
from flat.models import Country, Region, District, City
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
    return redirect('/geo/region/' + str(id) + '/add_child')


def add_city(request, id):
    citylistitems = City.objects.filter(region_id=id)
    citylist = []
    citylistchildren = {}
    for r in citylistitems:
        if r.pid:
            if r.pid not in citylistchildren:
                citylistchildren[r.pid] = []
            citylistchildren[r.pid].append(r)
        else:
            citylist.append(r)
    context = {
        'id': id,
        'citylist': citylist,
        'citylistchildren': citylistchildren
    }
    return render(request, 'geo/add_city.html', context)


def create_city(request, id):
    if request.method == 'POST':
        c = Region.objects.get(pk=id)
        r = City()
        r.region_id = id
        r.name = request.POST['name']
        r.save()
    return redirect('/geo/region/'+str(id)+'/add_city')


def city_delete(request, id):
    r = City.objects.get(pk=id)
    cid = r.region_id
    r.delete()
    return redirect('/geo/region/'+str(cid)+'/add_city')


def add_child_city(request, id):
    citylist = City.objects.filter(pid=id)
    context = {
        'id': id,
        'citylist': citylist
    }
    return render(request, 'geo/add_child_city.html', context)


def create_child_city(request, id):
    if request.method == 'POST':
        r2 = City.objects.get(pk=id)
        r = City()
        r.pid = r2
        r.region_id = r2.region_id
        r.name = request.POST['name']
        r.save()
    return redirect('/geo/city/' + str(id) + '/add_child')


def add_district(request, id):
    districtlist = District.objects.filter(city_id=id)
    context = {
        'id': id,
        'districtlist': districtlist
    }
    return render(request, 'geo/add_district.html', context)


def create_district(request, id):
    if request.method == 'POST':
        c = City.objects.get(pk=id)
        r = District()
        r.city_id = id
        r.name = request.POST['name']
        r.save()
    return redirect('/geo/city/' + str(id) + '/add_district')


def district_delete(request, id):
    r = District.objects.get(pk=id)
    cid = r.city_id
    r.delete()
    return redirect('/geo/region/'+str(cid)+'/add_district')