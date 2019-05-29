from django.shortcuts import render, redirect
from .models import ForumUser as User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from posts.models import Question, Answer
# Create your views here.
def register(request):
    context = {
        'title': 'Registro'
    }

    try:
        # Get data from request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
    except KeyError:
        return render(request, 'users/register.html', context)
    else:
        # Check if username is already taken
        users_res = User.objects.filter(username=username)
        if len(users_res) != 0:
            # context['error_message'] = "Nome de usuário já cadastrado! Escolha outro."
            context['email'] = email
            context['password'] = password
            context['first_name'] = first_name
            context['last_name'] = last_name
            context['fail'] = True
            context['username'] = username
        else:
            User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name, description="")
            context['success'] = True
            context['username'] = username
            # context['confirm_message'] = "Usuário {} cadastrado com sucesso!".format(username)
        return render(request, 'users/register.html', context)

@login_required
def profile(request):
    context = {}

    username = request.user.username

    user = User.objects.get(username=username)

    username = user.username
    email = user.email
    description = user.description
    first_name = user.first_name
    last_name = user.last_name
    context['username'] = username
    context['email'] = email
    if description:
        context['description'] = description
    if first_name:
        context['first_name'] = first_name
    if last_name:
        context['last_name'] = last_name

    # Activities tab
    questions = Question.objects.filter(user=user).order_by("-creation_date")[:3]
    context["questions"] = questions

    answers = Answer.objects.filter(user=user).order_by("-creation_date")[:3]
    context["answers"] = answers

    context["edit"] = True
    return render(request, 'users/profile.html', context)


def view_profile(request, username):
    context = {}

    if username == request.user.username:
        return redirect('users:profile')

    user = User.objects.get(username=username)

    username = user.username
    email = user.email
    description = user.description
    first_name = user.first_name
    last_name = user.last_name
    context['username'] = username
    context['email'] = email
    if description:
        context['description'] = description
    if first_name:
        context['first_name'] = first_name
    if last_name:
        context['last_name'] = last_name

    # Activities tab
    questions = Question.objects.filter(user=user).order_by("-creation_date")[:3]
    context["questions"] = questions

    answers = Answer.objects.filter(user=user).order_by("-creation_date")[:3]
    context["answers"] = answers

    context["edit"] = False
    return render(request, 'users/profile.html', context)



@login_required
def edit_profile(request):
    try:
        # Get data from request
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        description = request.POST['description']
    except KeyError:
        return redirect('users:profile')
    else:
        username = request.user.username

        user = User.objects.get(username=username)

        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.description = description

        new_pass = request.POST['password']
        if new_pass:
            user.set_password(new_pass)
        
        user.save()
        
    return redirect('users:profile')