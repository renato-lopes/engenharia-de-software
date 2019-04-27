from django.shortcuts import render

from users.models import ForumUser as User
from posts.models import Answer, Question

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

    users = User.objects.all()

    context['users'] = users

    return render(request, 'forum/users.html', context)


def all_posts(request):
    context = {
        'title': 'Perguntas'
    }
    return render(request, 'forum/posts.html', context)
