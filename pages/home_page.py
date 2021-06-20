from base.selenium_driver import SeleniumDriver
import base.custom_logger as cl
import logging
import time

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        self.driver = driver

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _header=                            "div#chrome-sticky-header"
    _my_account_icon =                  "div#myAccountDropdown"
    _account_filled =                   "div#myaccount-dropdown"
    _user_name_under_account_filled =   "//span[@class='tiqiyps' and contains(text(),'Hi {}')]"


    def verifyHomePageDisplay(self):
        time.sleep(2)
        if self.isElementDisplayed(self._header, "css") == False:
            self.log.info("can't find header element")
            return False
        self.log.info("Home page page display")


    def verifyUserLogedIn(self, firstName):
        if self.elementClick(self._my_account_icon, "css") == False:
            self.log.info("can't click on my account")
            return False

        accountEl = self.getElement(self._user_name_under_account_filled, "css")
        if accountEl == False:
            self.log.info("can't find my account filled element")
            return False

        tmpName = self._user_name_under_account_filled.format(firstName)
        childAccountEl = self.getChildElement(accountEl, tmpName, "xpath")
        breakpoint()

        if childAccountEl == False:
            self.log.info("can't find user name under my account filled")
            return False
        self.log.info("user verified ")
