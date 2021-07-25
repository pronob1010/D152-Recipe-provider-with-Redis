from . models import Recipe
from django.shortcuts import render

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def index(request):
    keyword = request.GET.get('serch')
    if cache.get(keyword):
        print("From cache.")
        recipes = cache.get(keyword)
    else:
        print("From DB.")
        if keyword:
            recipes = Recipe.objects.filter(title__contains=keyword)
            cache.set(keyword, recipes)
        else:
            recipes = Recipe.objects.all()
            
    return render(request, 'index.html', {'recipes':recipes})

def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'details.html', {'recipe':recipe})
