from django.shortcuts import render

from users.models import ForumUser as User
from posts.models import Answer, Question, Tag, QuestionTag

# Create your views here.
def index(request):
    context = {
        'title': 'Homepage'
    }
    questions = Question.objects.all().order_by("-creation_date")[:5]

    # Add post tags
    for question in questions:
        question_tags = QuestionTag.objects.filter(question=question)
        tags = []
        for el in question_tags:
            tags.append(el.tag)
        question.tags = tags

    context['questions'] = questions

    return render(request, 'forum/index.html', context)


def users(request):
    context = {
        'title': 'Usuários'
    }

    users = User.objects.all().order_by("username")
    questions = Question.objects.all().order_by("-creation_date")

    # Add post tags
    for question in questions:
        question_tags = QuestionTag.objects.filter(question=question)
        tags = []
        for el in question_tags:
            tags.append(el.tag)
        question.tags = tags

    context['posts'] = questions
    context['users'] = users

    return render(request, 'forum/users.html', context)


def all_posts(request):
    context = {
        'title': 'Perguntas'
    }

    questions = Question.objects.all().order_by("-creation_date")

    # Add post tags
    for question in questions:
        question_tags = QuestionTag.objects.filter(question=question)
        tags = []
        for el in question_tags:
            tags.append(el.tag)
        question.tags = tags

    context['posts'] = questions

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

    questions = Question.objects.all().order_by("-creation_date")

    # Add post tags
    for question in questions:
        question_tags = QuestionTag.objects.filter(question=question)
        tags = []
        for el in question_tags:
            tags.append(el.tag)
        question.tags = tags

    context['posts'] = questions
    
    return render(request, 'forum/about.html', context)