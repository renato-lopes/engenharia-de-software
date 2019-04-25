from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index , name='index'),
    path('users/', views.users , name='users'),
    path('create_question', views.create_question, name='create_question'),
]