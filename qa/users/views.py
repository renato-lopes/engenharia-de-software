from django.shortcuts import render

from .models import User

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
            new_user = User(username=username, email=email, password=password)
            new_user.save()
            context['confirm_message'] = "User {} sucessfully created!".format(username)
        return render(request, 'users/register.html', context)

def profile(request):
    context = {
        'title': 'Perfil'
    }
    return render(request, 'users/profile.html', context)