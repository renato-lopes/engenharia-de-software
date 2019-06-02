from django.test import TestCase
from users.models import ForumUser as User
from posts.models import *
from django.contrib.auth.models import User as AuthUser
from django.urls import reverse
from forum import views

class ViewTestCase(TestCase):
    question = None
    user = None
    answer = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_view(self):
        url = reverse('forum:index')
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)
    
    def test_users_view(self):
        url = reverse('forum:users')
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)

    def test_all_posts_view(self):
        url = reverse('forum:all_posts')
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)

    def test_all_tags_view(self):
        url = reverse('forum:all_tags')
        resp = self.client.get(url)
        self.assertTrue(str(resp.status_code)[0] != 4)
    