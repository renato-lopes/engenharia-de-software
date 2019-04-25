from django.shortcuts import render

from .models import *

def create_post(request):
    context = {
        'title': 'Nova Pergunta'
    }
    try:
        # Get data from request
        title = request.POST['title']
        description = request.POST['description']
    except KeyError:
        return render(request, 'posts/create_post.html', context)
    else:
        #TODO: Missing User
        
        new_question = Question(title=title, description=description)
        new_question.save()
        context['confirm_message'] = "Post {} sucessfully created!".format(title)
        return render(request, 'posts/create_post.html', context)