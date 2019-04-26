from django.shortcuts import render

from .models import *

def create_post(request):
    context = {
        'title': 'Nova Pergunta'
    }
    if not request.user.is_authenticated:
        return render(request, 'users/login.html', context)
    try:
        # Get data from request
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
    except KeyError:
        return render(request, 'posts/create_post.html', context)
    else:
        new_question = Question(title=title, description=description, user=request.user)
        new_question.save()
        context['confirm_message'] = "Post {} sucessfully created!".format(title)
        return render(request, 'posts/create_post.html', context)


def post(request):
    context = {
        'title': 'Pergunta'
    }
    return render(request, 'posts/post.html', context)
