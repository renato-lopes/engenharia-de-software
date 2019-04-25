from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    context = {
        'title': 'Homepage'
    }
    return render(request, 'forum/index.html', context)


def users(request):
    context = {
        'title': 'Usuários'
    }
    return render(request, 'forum/users.html', context)

