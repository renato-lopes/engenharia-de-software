from django.db import models

# Create your models here.
class Question(models.Model):
	description = models.CharField(max_length=8192)
	user = models.ForeignKey('users.User', on_delete=models.CASCADE)

class Answer(models.Model):
	description = models.CharField(max_length=8192)
	user = models.ForeignKey('users.User', on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Tags(models.Model):
	description = models.CharField(max_length=512)
	
class QuestionTags(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	tags = models.ForeignKey(Tags, on_delete=models.CASCADE)