from django.test import TestCase
from PutPutApp.models import *
from django.contrib.auth.models import User
class TestModels(TestCase):

    def setUp(self):
        self.player_user_type = User.objects.create(
            username = 'tigerwoods',
            password = 'testpassword',
            first_name = 'Tiger',
            last_name = 'Woods'
        )
        self.player_user_type.save()
        self.player_user_type.profile.player = True;
        self.player_user_type.profile.account_balance = 3;


    # TODO: can someone verify these 4 tests?
    def test_player_username(self):
        self.assertEquals(self.player_user_type.username, 'tigerwoods')

    def test_player_password(self):
        self.assertEquals(self.player_user_type.password, 'testpassword')

    def test_player_first_name(self):
        self.assertEquals(self.player_user_type.first_name, 'Tiger')

    def test_player_last_name(self):
        self.assertEquals(self.player_user_type.last_name, 'Woods')

    def test_player_account_balance(self):
        self.assertEquals(self.player_user_type.profile.account_balance, 3)

    def test_player_type(self):
        self.assertEquals(self.player_user_type.profile.player, True)

    # TODO: test all user types

    # TODO: test score

    # TODO: test drink

    # TODO: test orders

    # TODO: test calendar
