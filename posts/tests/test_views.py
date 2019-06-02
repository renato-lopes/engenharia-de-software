from django.test import TestCase
from users.models import ForumUser as User
from posts.models import *
from django.contrib.auth.models import User as AuthUser
from django.urls import reverse
from posts import views

class ViewTestCase(TestCase):
    question = None
    user = None
    answer = None

    def setUp(self):
        self.user = User.objects.create_user(username="questiontest", email="test@test", password="test", first_name="test", last_name="test", description="")
        self.question = Question.create(title="Test", description="Test example", tags='question_test_tag', user=self.user)
        self.answer = Answer.create(description="Test Answer", user=self.user, question=self.question)

    def tearDown(self):
        self.user.delete()
        self.answer.delete()
        self.question.delete()

    def test_create_post_view(self):
        url = reverse('posts:create_post')
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)
    
    def test_post_view(self):
        url = reverse('posts:post', kwargs={'id_post':self.question.id})
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)

    def test_edit_post_view(self):
        url = reverse('posts:edit_post', kwargs={'post_id':self.question.id})
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)

    def test_delete_post_view(self):
        url = reverse('posts:delete_post', kwargs={'post_id':self.question.id})
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)
    
    def test_edit_answer_view(self):
        url = reverse('posts:edit_answer', kwargs={'answer_id':self.answer.id})
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)
    
    def test_delete_answer_view(self):
        url = reverse('posts:delete_answer', kwargs={'answer_id':self.question.id})
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)