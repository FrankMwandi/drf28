from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        user = get_user_model()
        user = user.objects.create_user(
            username = 'tester',
            email ='tester@gmail.com',
            password = 'test12345'
        )
        self.assertEqual(user.username, 'tester')
        self.assertEqual(user.email, 'tester@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        user = get_user_model()
        admin_user = user.objects.create_superuser(
            username = 'admin',
            email ='tester@gmail.com',
            password = 'admin12345'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'tester@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)