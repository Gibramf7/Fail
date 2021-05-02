from django.shortcuts import render

# Create your views here.

def index(request):
    '''The home page for Pizzeria. '''
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)