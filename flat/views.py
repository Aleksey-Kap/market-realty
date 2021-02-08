from django.shortcuts import render, HttpResponse
from flat.models import *
# Create your views here.


def index(request):

    context = {
        'flatlist': Flat.objects.all(),
        'flatimges': Flatimges.objects.all(),
        'count': Flat.objects.filter().count(),
        'room_types': get_room_types(),
        'free_plan': get_free_plan(),
        'wc_type': get_wc_type(),
        'balcony_type': get_balcony_type(),
        'repair_type': get_repairtype_type(),
        'windows_view': get_windows_view(),
        'house_type': get_house_type(),
        'lift_type': get_lift_type(),
        'post': getpost(request),
        'post_room_types': get_post_room_types(request),
        'post_realty_types': get_post_realty_types(request),
        'get_operation_types_list': get_operation_types_list(),
    }
    return render(request, 'flat/index.html', context)


def snyat_kvartiru(request):
    q = Flat.objects.filter(isrent=1)
    context = {
        'flatlist': q,
        'flatimges': Flatimges.objects.all(),
        'count': q.count(),
        'room_types': get_room_types(),
        'free_plan': get_free_plan(),
        'wc_type': get_wc_type(),
        'balcony_type': get_balcony_type(),
        'repair_type': get_repairtype_type(),
        'windows_view': get_windows_view(),
        'house_type': get_house_type(),
        'lift_type': get_lift_type(),
        'post': getpost(request),
        'post_room_types': get_post_room_types(request),
        'post_realty_types': get_post_realty_types(request),
        'get_operation_types_list': get_operation_types_list(),
    }
    return render(request, 'flat/index.html', context)


def search(request):
    q = Flat.objects
    params = 0
    if 'price1' in request.POST and request.POST['price1']!='':
        params = 1
        q = q.filter(price__gte=request.POST['price1'])

    if 'price2' in request.POST and request.POST['price2']!='':
        params = 1
        q = q.filter(price__lte=request.POST['price2'])

    if 'room_types[]' in request.POST and len(request.POST.getlist('room_types[]'))>0:
        params = 1
        q = q.filter(roomtype_id__in=request.POST.getlist('room_types[]'))
    # return HttpResponse(str(request.POST.getlist('room_types[]')))

    # return HttpResponse(str(request.POST))

    if 'owner' in request.POST and '1' in request.POST['owner']:
        params = 1
        owner_item = get_saller_owner_item()

        q = q.filter(sallertype_id=owner_item.pk)


    if 'free_plan' in request.POST and len(request.POST.getlist('free_plan'))>0:
        params = 1
        q = q.filter(freeplan_id__in=request.POST.getlist('free_plan'))
    # return HttpResponse(str(request.POST.getlist('free_plan[]')))

    if 'wc_type' in request.POST and len(request.POST.getlist('wc_type'))>0:
        params = 1
        q = q.filter(wctype_id__in=request.POST.getlist('wc_type'))
    # return HttpResponse(str(request.POST.getlist('free_plan[]')))

    if 'balcony_type' in request.POST and request.POST['balcony_type']==1:
        params = 1
        q = q.filter(balcony_id__gt=0)

    if 'balcony_type' in request.POST and request.POST['balcony_type']==2:
        params = 1
        q = q.filter(loggia_id__gt=0)

    if 'repair_type' in request.POST and len(request.POST.getlist('repair_type'))>0:
        params = 1
        q = q.filter(repairtype_id__in=request.POST.getlist('repair_type'))
    # return HttpResponse(str(request.POST.getlist('free_plan[]')))

    if 'windows_view' in request.POST and len(request.POST.getlist('windows_view'))>0:
        params = 1
        q = q.filter(windowsview_id__in=request.POST.getlist('windows_view'))
    # return HttpResponse(str(request.POST.getlist('free_plan[]')))

    if 'house_type' in request.POST and len(request.POST.getlist('house_type'))>0:
        params = 1
        q = q.filter(housetype_id__in=request.POST.getlist('house_type'))
    # return HttpResponse(str(request.POST.getlist('free_plan[]')))

    if 'lift_type' in request.POST and len(request.POST.getlist('lift_type'))>0:
        params = 1
        q = q.filter(lifttype_id__in=request.POST.getlist('lift_type'))
    # return HttpResponse(str(request.POST.getlist('free_plan[]')))


    if 'realty_type[]' in request.POST and len(request.POST.getlist('realty_type[]'))>0:
        rt = request.POST.getlist('realty_type[]')
        if '1' in rt and '2' not in rt:
            params = 1
            q = q.filter(isnew=1)

        if '2' in rt and '1' not in rt:
            params = 1
            q = q.filter(isnew=0)

    # return HttpResponse(str(request.POST.getlist('free_plan[]')))


    if 'floor1' in request.POST and request.POST['floor1']!='':
        params = 1
        q = q.filter(floor__gte=request.POST['floor1'])

    if 'floor2' in request.POST and request.POST['floor2']!='':
        params = 1
        q = q.filter(floor__lte=request.POST['floor2'])

    if 'floortotal1' in request.POST and request.POST['floortotal1'] != '':
        params = 1
        q = q.filter(floortotal__gte=request.POST['floortotal1'])

    if 'floortotal2' in request.POST and request.POST['floortotal2'] != '':
        params = 1
        q = q.filter(floortotal__lte=request.POST['floortotal2'])

    if 'year1' in request.POST and request.POST['year1'] != '':
        params = 1
        q = q.filter(year__gte=request.POST['year1'])

    if 'year2' in request.POST and request.POST['year2'] != '':
        params = 1
        q = q.filter(year__lte=request.POST['year2'])


    if 'operation_type' in request.POST:
        if request.POST['operation_type'] == 'buy':
            params = 1
            q = q.filter(issale=1)
        elif request.POST['operation_type'] == 'rent_month':
            params = 1
            q = q.filter(isrent=1)
        elif request.POST['operation_type'] == 'rent_day':
            params = 1
            q = q.filter(isdayly=1)

    if 'sqtotal1' in request.POST and request.POST['sqtotal1']!='':
        params = 1
        q = q.filter(sqtotal__gte=request.POST['sqtotal1'])

    if 'sqtotal2' in request.POST and request.POST['sqtotal2']!='':
        params = 1
        q = q.filter(sqtotal__lte=request.POST['sqtotal2'])

    if 'sqkitchen1' in request.POST and request.POST['sqkitchen1']!='':
        params = 1
        q = q.filter(sqkitchen__gte=request.POST['sqkitchen1'])

    if 'sqkitchen2' in request.POST and request.POST['sqkitchen2']!='':
        params = 1
        q = q.filter(sqkitchen__lte=request.POST['sqkitchen2'])


    if not params:
        q = q.all()




    context = {
        'flatlist': q,
        'flatimges': Flatimges.objects.all(),
        'count': q.count(),
        'room_types': get_room_types(),
        'free_plan': get_free_plan(),
        'wc_type': get_wc_type(),
        'balcony_type': get_balcony_type(),
        'repair_type': get_repairtype_type(),
        'windows_view': get_windows_view(),
        'house_type': get_house_type(),
        'lift_type': get_lift_type(),
        'post': getpost(request),
        'post_room_types': get_post_room_types(request),
        'post_realty_types': get_post_realty_types(request),
        'get_operation_types_list': get_operation_types_list(),

    }
    return render(request, 'flat/index.html', context)


def getpost(request):
    return {
        'price1': request.POST['price1'] if 'price1' in request.POST else "",
        'price2': request.POST['price2'] if 'price2' in request.POST else "",
        'operation_type': request.POST['operation_type'] if 'operation_type' in request.POST else "",
        'owner': 1 if 'owner' in request.POST and '1' in request.POST['owner'] else 0,
        'balcony_type': request.POST['balcony_type'] if 'balcony_type' in request.POST else "0"

    }


def get_post_realty_types(request):
    return list(map(int, request.POST.getlist('realty_type[]')))

def get_post_room_types(request):
    return list(map(int, request.POST.getlist('room_types[]')))


def get_operation_types_list():
    return {
        "buy": "Купить",
        "rent_month": "Снять",
        "rent_day": "Посуточно"
    }



def get_room_types():
    return Roomtypes.objects.all()

def get_saller_owner_item():
    return Sallertype.objects.filter(name='Собственник').get()

def get_free_plan():
    return Freeplan.objects.all()

def get_wc_type():
    return Wctype.objects.all()

def get_balcony_type():
    return Balcony.objects.all()

def get_loggia_type():
    return Loggia.objects.all()

def get_repairtype_type():
    return Repairtype.objects.all()

def get_windows_view():
    return Windowsview.objects.all()

def get_house_type():
    return Housetype.objects.all()

def get_lift_type():
    return Lifttype.objects.all()

def card(request, id):
    f = Flat.objects.get(pk=id)
    context = {'id': id,
               'f': f,
               'flatimges': Flatimges.objects.all(),
               'count': Flatimges.objects.count(),


               }
    return render(request, 'flat/card.html', context)