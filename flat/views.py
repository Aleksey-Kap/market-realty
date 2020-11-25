from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        'flatlist': range(1, 10)
    }
    return render(request, 'flat/index.html', context)


def card(request, id):
    context = {'id' : id}
    return render(request, 'flat/card.html', context)