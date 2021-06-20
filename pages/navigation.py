from base.selenium_driver import SeleniumDriver
import base.custom_logger as cl
import logging
from pages.signUp import SignUp
import time

class Navigation(SeleniumDriver):

    def __init__(self, driver):
        self.driver = driver
        self.sn = SignUp(self.driver)

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _my_account_icon =  "div#myAccountDropdown"
    _signIn_button =    "//a[contains(@href,'register')]"

    def navigateToSingInPage(self):
        if self.elementClick(self._my_account_icon, "css") == False:
            self.log.info("can't click on my account")
            return False
        time.sleep(1)

        if self.elementClick(self._signIn_button, "Xpath") == False:
            self.log.info("can't click on join button")
            return False

        if self.sn.verifySignInPageDisplay() == False:
            self.log.info("register page isn't display")
            return False