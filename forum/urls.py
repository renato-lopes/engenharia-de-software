from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index , name='index'),
    path('users/', views.users , name='users'),
    path('all-posts/', views.all_posts , name='all_posts'),
    path('all-tags/', views.all_tags, name='all_tags'),
    path('about/', views.about, name='about')
]

