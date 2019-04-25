from django.db import models

# Create your models here.
class Question(models.Model):
	title = description = models.CharField(max_length=512)
	description = models.TextField()
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey('users.User', on_delete=models.CASCADE)

class Answer(models.Model):
	description = models.TextField()
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey('users.User', on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Tags(models.Model):
	description = models.CharField(max_length=512)
	
class QuestionTags(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	tags = models.ForeignKey(Tags, on_delete=models.CASCADE)	