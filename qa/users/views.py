from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

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
    except KeyError:
        return render(request, 'users/register.html', context)
    else:
        # Check if username is already taken
        users_res = User.objects.filter(username=username)
        if len(users_res) != 0:
            context['error_message'] = "Username already taken!"
        else:
            User.objects.create_user(username, email, password)
            context['confirm_message'] = "User {} sucessfully created!".format(username)
        return render(request, 'users/register.html', context)

@login_required
def profile(request):
    context = {}

    user = request.user

    username = user.username
    email = user.email
    context['username'] = username
    context['email'] = email

    return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request):
    try:
        # Get data from request
        email = request.POST['email']
    except KeyError:
        return redirect('users:profile')
    else:
        user = request.user

        if email:
            user.email = email
            user.save()
        
    return redirect('users:profile')