from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse('<h1>Bienvenue sur ma communauté de devs.</h1>')


def member_view(request, member_id):
    return HttpResponse('<h1>Affichage du membre numéro {}</h1>'.format(member_id))
