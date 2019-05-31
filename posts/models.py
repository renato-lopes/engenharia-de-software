from django.db import models
from django.urls import reverse
from users.models import ForumUser as User
from django.contrib.auth.models import User as AuthUser

# Create your models here.
class Question(models.Model):
	title = description = models.CharField(max_length=512)
	description = models.TextField()
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	upvote = models.ManyToManyField(AuthUser, related_name="upvote", blank=True)
	downvote = models.ManyToManyField(AuthUser, related_name="downvote", blank=True)

	def get_absolute_url(self):
		return reverse("posts:post", kwargs={"id_post": self.id})

	def get_like_url(self, post_id):
		return reverse("posts:like_toggle")

class Answer(models.Model):
	description = models.TextField()
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	upvote = models.ManyToManyField(AuthUser, related_name="a_upvote", blank=True)
	downvote = models.ManyToManyField(AuthUser, related_name="a_downvote", blank=True)

	def get_question(self):
		return self.question



class Tag(models.Model):
	name = models.CharField(max_length=512)
	
class QuestionTag(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)	