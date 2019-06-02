from django.test import TestCase
from users.models import ForumUser as User
from posts.models import *
from django.contrib.auth.models import User as AuthUser

class QuestionTestCase(TestCase):
    user = None
    question = None

    def setUp(self):
        self.user = User.objects.create_user(username="questiontest", email="test@test", password="test", first_name="test", last_name="test", description="")
        self.question = Question.create(title="Test", description="Test example", tags='question_test_tag', user=self.user)
    def tearDown(self):
        self.user.delete()
        self.question.delete()

    def test_simple(self):
        a = 10 + 20
        self.assertEqual(a, 30)
    
    def test_create_question(self):
        self.assertEqual(self.question.title, "Test")
        self.assertEqual(self.question.description, "Test example")

    def test_search_question(self):
        q = Question.search(title="Test")
        self.assertEqual(q[0].title, "Test")

    def test_read_question(self):
        q = Question.read(id=self.question.id)
        self.assertEqual(q.id, self.question.id)
    
    def test_update_question(self):
        q = Question.update(id=self.question.id, title="TestTest", description="Test example Test", tags='question_test_tag')
        self.assertEqual(q.title, "TestTest")
        self.assertEqual(q.description, "Test example Test")