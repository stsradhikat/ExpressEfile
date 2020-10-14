
from  PageObjects.Locators.HomePageLocators import LocatorAddress

class HomePage():

    def __init__(self,driver):
        self.driver = driver



    def verifySignIn(self):

        print(self.driver.find_element_by_xpath(LocatorAddress.button_logout_xpath).is_displayed())
        assert self.driver.find_element_by_xpath(LocatorAddress.button_logout_xpath).is_displayed()=="True"

        #self.asserTrue(self.driver.find_element_by_xpath(LocatorAddress.button_logout_xpath).is_displayed()=="False")

