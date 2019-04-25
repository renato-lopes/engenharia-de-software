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

def create_question(request):
    context = {
        'title': 'Nova Pergunta'
    }
    try:
        # Get data from request
        title = request.POST['title']
        description = request.POST['description']
    except KeyError:
        return render(request, 'forum/create_question.html', context)
    else:
        #TODO: Missing User
        
        new_question = Question(title=title, description=description)
        new_question.save()
        context['confirm_message'] = "Question {} sucessfully created!".format(title)
        return render(request, 'forum/create_question.html', context)