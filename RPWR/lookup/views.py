import re
from . models import Recipe
from django.shortcuts import render

# Create your views here.
def index(request):
    keyword = request.GET.get('serch')
    if keyword:
        recipes = Recipe.objects.filter(title__contains=keyword)
    else:
        recipes = Recipe.objects.all()
        
    return render(request, 'index.html', {'recipes':recipes})

def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'details.html', {'recipe':recipe})