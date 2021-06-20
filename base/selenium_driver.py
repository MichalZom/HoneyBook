from selenium.webdriver.common.by import By
import base.custom_logger as cl
import logging


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.debug("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.debug("Element Found with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.debug("Element not found with locator: " + locator + " locatorType: " + locatorType)
            return False
        return element

    # Either provide element or a combination of locator and locatorType
    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.debug("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.debug("Cannot click on the element with locator: " + locator +" locatorType: " + locatorType)
            return False

    # Either provide element or a combination of locator and locatorType
    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:
                el = self.getElement(locator, locatorType)
                if el == False:
                    self.log.debug("Cannot find element with locator: " + locator + " locatorType: " + locatorType)
                    return False
            elif element:
                element.send_keys(data)
            self.log.debug("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.debug("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            return False


        # Check if element is displayed
        # Either provide element or a combination of locator and locatorType
    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.debug("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.debug("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.debug("Element not found with locator: " + locator +
                           " locatorType: " + locatorType)
            return False

    def getChildElement(self, parentElement, childLocator, childLocatorType="id"):
        cElement = None
        try:
            cLocatorType = childLocatorType.lower()
            byType = self.getByType(cLocatorType)
            cElement = parentElement.find_element(byType, childLocator)
            self.log.debug("Child element Found with locator: " + childLocator + " locatorType: " + childLocatorType)
        except:
            self.log.debug("Child element not found with locator: " + childLocator + " locatorType: " + childLocatorType)
            return False
        return cElement



