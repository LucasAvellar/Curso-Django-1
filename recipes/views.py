from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'recipes/home.html',context={
        'name':'Lucas Avellar'
    })

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('contato')