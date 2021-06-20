import pytest
import base.custom_logger as cl
import logging
import unittest
from pages.navigation import Navigation
from pages.signUp import SignUp
from pages.home_page import HomePage
from base.enums import *
from faker import Faker


class Register(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, setUp):
        self.fake = Faker()
        self.nav = Navigation(self.driver)
        self.sn = SignUp(self.driver)
        self.hp = HomePage(self.driver)
        self.log = cl.customLogger(logging.DEBUG)

    @pytest.mark.run(order=1)
    def test_1(self):
        self.log.info("STARTING TEST_1 : Sign up (Join)")
        assert self.nav.navigateToSingInPage() != False , "Failed navigate to sign in page"
        preferences = [Preferences.EXCLUSIVES.value ,Preferences.ASOS_PARTNERS.value]
        assert self.sn.fillInRegisterForm(self.fake.email(),"michal", "zom", "1234567899","20.11.1990",
                                    Gender.MALE.value, preferences) != False, "Failed to fill in registration form"
        assert self.hp.verifyHomePageDisplay() != False, "Failed verify home page display after finish registration"

    @pytest.mark.run(order=2)
    def test_2(self):
        breakpoint()
        self.log.info("STARTING TEST_2 : Sign up (Join) validations")
        assert self.hp.verifyUserLogedIn("michal") != False , "Failed verify user is logged in "

