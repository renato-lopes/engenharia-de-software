from django.shortcuts import render

from users.models import ForumUser as User
from posts.models import Answer, Question, Tag

# Create your views here.
def index(request):
    context = {
        'title': 'Homepage'
    }
    questions = Question.objects.all().order_by("-creation_date")[:5]
    context['questions'] = questions

    return render(request, 'forum/index.html', context)


def users(request):
    context = {
        'title': 'Usuários'
    }

    users = User.objects.all().order_by("username")

    context['users'] = users

    return render(request, 'forum/users.html', context)


def all_posts(request):
    context = {
        'title': 'Perguntas'
    }

    questions = Question.objects.all().order_by("-creation_date")
    context['posts'] = questions
    
    tags = Tag.objects.all()
    context['tags'] = tags

    return render(request, 'forum/posts.html', context)

def all_tags(request):
    context = {
        'title': 'Tags'
    }

    tags = Tag.objects.all()
    context['tags'] = tags

    return render(request, 'forum/tags.html', context)

def about(request):
    context = {
        'title': 'Sobre'
    }
    return render(request, 'forum/about.html', context)