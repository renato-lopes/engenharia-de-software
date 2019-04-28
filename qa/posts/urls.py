from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('post/', views.post, name='post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:id_post>/', views.post, name='post'),
    path('tag/<int:tag_id>/', views.tag, name='tag'),
    path('edit_answer/<int:answer_id>/', views.edit_answer, name='edit_answer'),
    path('delete_answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
    path('tag/<int:tag_id>/', views.tag, name='tag')
]





