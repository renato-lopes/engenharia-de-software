from django.shortcuts import render

# Create your views here.
def register(request):
    context = {
        'title': 'Registro'
    }

    return render(request, 'users/register.html', context)

def profile(request):
    context = {
        'title': 'Perfil'
    }
    return render(request, 'users/profile.html', context)