from django.test import TestCase

class QuestionTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_simple(self):
        a = 10 + 20
        self.assertEqual(a, 30)