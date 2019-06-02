from django.test import TestCase, Client
from users.models import ForumUser as User
from posts.models import *
from django.contrib.auth.models import User as AuthUser
from django.urls import reverse
from users.views import *

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

    def test_register_view(self):
        url = reverse('users:register')
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)
    
    def test_profile_view(self):
        self.client.force_login(self.user, backend=None)
        url = reverse('users:profile')
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)

    def test_view_profile_view(self):
        # self.client.force_login(self.user, backend=None)
        url = reverse('users:view_profile', kwargs={'username':self.user.username})
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)
    
    def test_edit_profile_view(self):
        self.client.force_login(self.user, backend=None)
        url = reverse('users:edit_profile')
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)