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
        # for tag_name in tags.split(', '):
        #     if(len(tag_name) == 0):
        #         continue
        #     tag_res = Tags.objects.filter(name=tag_name)
        #     if (len(tag_res) == 0):
        #         new_tag = Tag(name=tag_name)
        #         new_tag.save()
        #     else:
        #         new_tag = tag_res[0]
        #     new_question_tag = QuestionTag(question=new_question, tag=new_tag)
        #     new_question_tag.save()
        return redirect("/all-posts") # TODO: redirect to post page


def post(request,id_post):

    readed_question = Question.objects.get(id=id_post) #questao clicada pelo usuario


    context = {"question": readed_question}


    return render(request, 'posts/post.html', context)
