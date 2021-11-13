from django.test import TestCase
from PutPutApp.models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.create(firstname="Tiger", lastname="Woods", user_type="Player", account_balance="12.95")


    def test_user_details(self):
        player = Profile.get(firstname="Tiger")
        self.assertEqual(player.is_player(), True)
