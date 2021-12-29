from django.test import TestCase
from config.tests import BaseTestCase
from .models import User, UserProfile
import datetime

# Create your tests here.



class UserTestCase(BaseTestCase):

    def test_user_creation(self):
        """
        Test that a user can be created
        """
        User.objects.create_user(
            username="test_user",
            email="test_user@example.com",
            password="test_password"
        )

        new_user = User.objects.get(username="test_user")
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user.username, "test_user")

    def test_user_profile_creation(self):
        """
        Test that a user profile is created when a user is created
        """
        User.objects.create_user(
            username="test_user_1",
            email="test_user_1@example.com",
        )
        new_user_1 = User.objects.get(username="test_user_1")
        self.assertIsNotNone(new_user_1.profile)
        self.assertEqual(new_user_1.email, new_user_1.profile.email)

    def test_user_can_edit_profile(self):
        """
        Test that a user can edit their profile
        """
        User.objects.create_user(
            username="test_user_2",
            email="test_user_2@example.com",
        )
        profile = UserProfile.objects.get(user__username="test_user_2")
        profile.first_name = "Test"
        profile.last_name = "User"
        profile.middle_name = "middle name"
        profile.dob = datetime.date(2003,10,12)
        profile.save()
        self.assertEqual(profile.first_name, "Test")
        self.assertEqual(profile.last_name, "User")
        self.assertEqual(profile.middle_name, "middle name")
        self.assertEqual(profile.dob,datetime.date(2003,10,12))
