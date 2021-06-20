from base.selenium_driver import SeleniumDriver
import base.custom_logger as cl
import logging
import datetime
from selenium.webdriver.support.ui import Select


class SignUp(SeleniumDriver):

    def __init__(self, driver):
        self.driver = driver

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _register_form =    "div#register-form"
    _email_parent =     "div.input-wrapper[aria-labelledby=EmailLabel]"
    _email =            "Email"
    _first_name_parent ="div.input-wrapper[aria-labelledby=FirstNameLabel]"
    _first_name =       "FirstName"
    _last_name_parent = "div.input-wrapper[aria-labelledby=LastNameLabel]"
    _last_name =        "LastName"
    _password_parent =  "div.input-wrapper[aria-labelledby=PasswordLabel]"
    _password =         "Password"
    _birthday_day =     "BirthDay"
    _birthday_month =   "BirthMonth"
    _birthday_year =    "BirthYear"
    _interested_in =    "input#{}"
    _preference =       "div#{}"
    _register_button =  "input#register"


    def verifySignInPageDisplay(self):
        if self.isElementDisplayed(self._register_form, "css") == False:
            self.log.info("can't find register form in page")
            return False
        self.log.info("sign up page display")

    def fillInRegisterForm(self,email, firstName, lastName, password, birthDate, interested="", preferences=""):
        if self.insertFormData(email,self._email_parent, self._email, parentLocatorType="css") == False:
            self.log.info("can't insert email address")
            return False

        if self.insertFormData(firstName, self._first_name_parent, self._first_name, parentLocatorType="css") == False:
            self.log.info("can't insert first name")
            return False

        if self.insertFormData(lastName, self._last_name_parent, self._last_name, parentLocatorType="css") == False:
            self.log.info("can't insert last name")
            return False

        if self.insertFormData(password, self._password_parent, self._password, parentLocatorType="css") == False:
            self.log.info("can't insert password")
            return False

        if self.setBirthDate(birthDate) == False:
            self.log.info("can't set birthdate date")
            return False

        tmp = self._interested_in.format(interested)
        if self.elementClick(tmp, "css") == False:
            self.log.info("can't choose 'mostly interested in' option")
            return False

        if self.chooseContactPreferences(preferences) == False:
            self.log.info("can't set preferences")
            return False

        if self.elementClick(self._register_button, "css") == False:
            self.log.info("can't click on register button")
            return False

        self.log.info("Registration form was filled successful")


    def insertFormData(self, data, parentLocator,  childLocator, parentLocatorType="id", childLocatorType="id"):
        parentEl= self.getElement(parentLocator, parentLocatorType)
        if parentEl == False:
            self.log.info("can't find parent locator textbox")
            return False

        childEl = self.getChildElement(parentEl, childLocator, childLocatorType)
        if childEl == False:
            self.log.info("can't find child locator textbox")
            return False

        if self.sendKeys(data, element=childEl) == False:
            self.log.info("can't insert data")
            return False

        self.log.info("insert data was successful")


    def setBirthDate(self, date):
        d = datetime.datetime.strptime(date, '%d.%m.%Y')
        month = d.strftime("%B")
        tmpDate = date.split(".")

        if self.selectDate(self._birthday_day, "value", tmpDate[0]) == False:
            self.log.info("can't choose birthday day")
            return False

        if self.selectDate(self._birthday_month, "text", month) == False:
            self.log.info("can't choose birthday month")
            return False

        if self.selectDate(self._birthday_year, "value", tmpDate[2]) == False:
            self.log.info("can't choose birthday year")
            return False

        self.log.info("set birthdate was successful")

    def selectDate(self,selectLocator, byType, value):
        try:
            select = Select(self.getElement(selectLocator))
            if byType == "text":
                select.select_by_visible_text(value)
            elif byType == "value":
                select.select_by_value(value)
        except:
            self.log.info("can't choose select value")
            return False

    def chooseContactPreferences(self, preferences):
        if type(preferences) is list:
            for preference in preferences:
                tmp = self._preference.format(preference)
                if self.elementClick(tmp,"css") == False:
                    self.log.info("can't choose preference '" + preference)
                    return False
        else:
            tmp = self._preference.format(preferences)
            if self.elementClick(tmp,"css") == False:
                self.log.info("can't choose preference '" + preferences)
                return False

        self.log.info("chosen preferences was successful")

