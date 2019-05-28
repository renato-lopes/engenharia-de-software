from django.db import models
from users.models import ForumUser as User

# Create your models here.
class Question(models.Model):
	title = description = models.CharField(max_length=512)
	description = models.TextField()
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	upvote = models.IntegerField()
	downvote = models.IntegerField()

class Answer(models.Model):
	description = models.TextField()
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	upvote = models.IntegerField()
	downvote = models.IntegerField()

class Tag(models.Model):
	name = models.CharField(max_length=512)
	
class QuestionTag(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)	