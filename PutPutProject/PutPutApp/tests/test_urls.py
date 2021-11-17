from django.test import SimpleTestCase
from django.urls import reverse, resolve
from PutPutApp.views import *

class TestUrls(SimpleTestCase):

    def test_dashboard_url_resolved(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)

    # User Account Pages-------------------------
    def test_registration_url_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    # TODO: resolve error
    # def test_login_url_resolved(self):
    #     url = reverse('Login')
    #     self.assertEquals(resolve(url).func, login)

    # TODO: research how to test account page if necessary
    # def test_accounts_url_resolved(self):
    #     url = reverse('accounts')
    #     self.assertEquals(resolve(url).func, accounts)

    def test_manageusers_url_resolved(self):
        url = reverse('manage_users')
        self.assertEquals(resolve(url).func, manage_users)

    # Tavern Pages----------------------------
    def test_menu_url_resolved(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func, menu)

    def test_managemenu_url_resolved(self):
        url = reverse('manage_menu')
        self.assertEquals(resolve(url).func, manage_menu)

    def test_orders_url_resolved(self):
        url = reverse('orders')
        self.assertEquals(resolve(url).func, orders)

    # TODO: research how to test order fulfillment, maybe in views?

    # Score pages-------------------------------
    def test_leaderboard_url_resolved(self):
        url = reverse('leaderboard')
        self.assertEquals(resolve(url).func, leaderboard)

    def test_scorecard_url_resolved(self):
        url = reverse('scorecard')
        self.assertEquals(resolve(url).func, scorecard)



