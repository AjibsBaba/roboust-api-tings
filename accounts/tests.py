import uuid

from django.test import TestCase

from accounts.models import User


class AccountTest(TestCase):
    def setUp(self):
        User.objects.create(id=uuid.uuid4(), email='samuel@robustapi.com', first_name='Samuel', last_name='Ajibade',
                            is_active=True, is_superuser=False)
        User.objects.create(id=uuid.uuid4(), email='kunle@robustapi.com', first_name='Kunle', last_name='Afod',
                            is_active=True, is_superuser=False)

    def test_users_have_emails(self):
        """
        Users are correctly identified with their email addresses
        """
        samuel = User.objects.get(email='samuel@robustapi.com')
        kunle = User.objects.get(email='kunle@robustapi.com')
        self.assertEqual(samuel.has_email(), 'samuel@robustapi.com')
        self.assertEqual(kunle.has_email(), 'kunle@robustapi.com')
