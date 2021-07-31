from django.shortcuts import render
from .models import Pets
# Create your views here.


def index(request):

    pets= Pets.objects.all()
    return render(request, "index.html",{'pets' : pets})