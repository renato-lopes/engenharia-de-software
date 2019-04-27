from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.models import ForumUser as User

from .models import *

@login_required
def create_post(request):
    context = {}
    try:
        # Get data from request
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
    except KeyError:
        return render(request, 'posts/create_post.html', context)
    else:
        username = request.user.username
        user = User.objects.get(username=username)
        new_question = Question(title=title, description=description, user=user)
        new_question.save()
        return redirect("/all-posts") # TODO: redirect to post page


def post(request):
    context = {
        'title': 'Pergunta'
    }
    return render(request, 'posts/post.html', context)
