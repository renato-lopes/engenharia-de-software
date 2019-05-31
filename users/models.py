from django.db import models
from django.contrib.auth.models import User

class ForumUser(User):
    description = models.TextField()
    photo = models.ImageField(upload_to='images/', default='images/user.ico')