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

	def create(title, description, tags, user):
		question = Question(title=title, description=description, user=user)
		question.save()
		QuestionTag.assign_tags_to_questions(question, tags)
		return question

	def search(**kwargs):
		result = Question.objects.filter(**kwargs)
		questions = []
		for el in result:
			questions.append(Question.get(el.id))
		return questions

	def read(id):
		try:
			question = Question.objects.get(id= id)
		except:
			question = None
		return question

	def update(id, title, description, tags):
		question = Question.read(id)
		question.title = title
		question.description = description
		question.save()
		QuestionTag.assign_tags_to_questions(question, tags)
		return question

	def remove(id):
		question = Question.read(id)
		question.delete()

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

	def create(description, user, question):
		answer = Answer(description=description, user=user, question=question)
		answer.save()
		return answer

	def search(**kwargs):
		result = Answer.objects.filter(**kwargs)
		answers = []
		for el in result:
			answers.append(Answer.get(el.id))
		return answers

	def read(id):
		try:
			answer = Answer.objects.get(id= id)
		except:
			answer = None
		return answer

	def update(id, description):
		answer = Answer.read(id)
		answer.description = description
		answer.save()
		return answer

	def remove(id):
		answer = Answer.read(id)
		answer.delete()

	def get_question(self):
		return self.question

class Tag(models.Model):
	name = models.CharField(max_length=512)

	def create(name):
		tag = Tag(name=name)
		tag.save()
		return tag

	def read(id):
		try:
			tag = Tag.objects.get(id= id)
		except:
			tag = None
		return tag

	def search(**kwargs):
		tags = []
		result = Tag.objects.filter(**kwargs)
		for el in result:
			tags.append(Tag.objects.get(id= el.id))
		return tags

	def update(name):
		tag = Tag.read(id)
		tag.name = name
		tag.save()
		return tag
	
	def delete(id):
		tag = Tag.read(id)
		tag.delete()

class QuestionTag(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

	def create(question, tag):
		question_tag = QuestionTag(question=question, tag=tag)
		question_tag.save()
		return tag

	def assign_tags_to_questions(question, tags):
		question_tags = QuestionTag.search(question=question)
		for qt in question_tags:
			qt.delete()
		
		for tag_name in tags.split(','):
			if(len(tag_name) == 0):
				continue
			tag_name = tag_name.strip()
			tag_res = Tag.search(name=tag_name)
			if (len(tag_res) == 0):
				tag = Tag.create(name=tag_name)
			else:
				tag = tag_res[0]
			QuestionTag.create(question, tag);
			

	def	search(**kwargs):
		question_tags = []
		result = QuestionTag.objects.filter(**kwargs)
		for el in result:
			question_tags.append(QuestionTag.objects.get(id=el.id))
		return question_tags