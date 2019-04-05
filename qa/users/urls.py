from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
] 