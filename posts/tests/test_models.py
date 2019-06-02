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

class AnswerTestCase(TestCase):
    user = None
    question = None
    answer = None

    def setUp(self):
        self.user = User.objects.create_user(username="questiontest", email="test@test", password="test", first_name="test", last_name="test", description="")
        self.question = Question.create(title="Test", description="Test example", tags='question_test_tag', user=self.user)
        self.answer = Answer.create(description="Test Answer", user=self.user, question=self.question)
    
    def tearDown(self):
        self.user.delete()
        self.question.delete()
    
    def test_create_answer(self):
        self.assertEqual(self.answer.description, "Test Answer")

    def test_search_anwser(self):
        a = Answer.search(description="Test Answer")
        self.assertEqual(a[0].description, "Test Answer")

    def test_read_answer(self):
        a = Answer.read(id=self.answer.id)
        self.assertEqual(a.id, self.answer.id)
    
    def test_update_answer(self):
        a = Answer.update(id=self.question.id, description="Test modified Test")
        self.assertEqual(a.description, "Test modified Test")