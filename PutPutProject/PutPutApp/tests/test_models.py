from django.test import TestCase
from PutPutApp.models import *

class TestModels(TestCase):

    def setUp(self):
        self.player_user_type = Profile.objects.create(
            account_balance = 3,
            firstname = 'Tiger',
            lastname = 'Woods',
            player = True,
        )

    # TODO: can someone verify this?
    def test_player_firstname(self):
        self.assertEquals(self.player_user_type.firstname, 'Tiger')

    def test_player_lastname(self):
        self.assertEquals(self.player_user_type.lastname, 'Woods')

    def test_player_account_balance(self):
        self.assertEquals(self.player_user_type.account_balance, '3')

    def test_player_type(self):
        self.assertEquals(self.player_user_type.player, 'True')

    # TODO: test all user types

    # TODO: test score

    # TODO: test drink

    # TODO: test orders

    # TODO: test calendar