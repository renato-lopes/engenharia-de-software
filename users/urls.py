from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/', auth_views.LoginView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_profile/<str:username>/', views.view_profile, name='view_profile')
] 