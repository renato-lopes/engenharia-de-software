from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
<<<<<<< HEAD
    path('post/', views.post, name='post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
=======
    path('post/<int:id_post>/', views.post, name='post'),
    path('post/', views.post, name='post'), 
>>>>>>> ba810fa80931ea83acc61a648e4ecb6f8261adb4
]





