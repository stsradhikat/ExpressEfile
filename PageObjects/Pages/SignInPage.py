from  PageObjects.Locators.SignInPageLocators import LocatorAddress
from Parent.SeleniumBase import Base


class SignInPage():
    global bobj
    bobj = Base()
    def __init__(self,driver):
        self.driver = driver

       # self.button_signin_id = LocatorAddress.button_signin_id
       # self.textbox_emailAddress_Xpath=LocatorAddress.textbox_emailAddress_Xpath

    def clickSignIn(self):
        self.driver.find_element_by_id(LocatorAddress.button_signin_id).click()


    def setEmailAddress(self,email):
        self.driver.find_element_by_xpath(LocatorAddress.textbox_emailAddress_Xpath).clear()

        self.driver.find_element_by_xpath(LocatorAddress.textbox_emailAddress_Xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(LocatorAddress.textbox_password_Xpath).clear()

        self.driver.find_element_by_xpath(LocatorAddress.textbox_password_Xpath).send_keys(password)
    def clickPopUpSignIn(self):
        self.driver.find_element_by_id(LocatorAddress.button_popupsignin_id).click()

    def verifyGoogleSignInAccount(self):
            actmsg = str(self.driver.find_element_by_xpath(LocatorAddress.msg_google_account_xpath).text)
            expmsg = "You have already registered with Google account, please sign-in using Google"
            bobj.verifyText(actmsg,expmsg)


    def verifyFacebookSignInAccount(self):
            actmsg = str(self.driver.find_element_by_xpath(LocatorAddress.msg_google_account_xpath).text)
            expmsg="You have already registered with Facebook account, please sign-in using Facebook"
            bobj.verifyText(actmsg,expmsg)
    def verifyUnRegisteredAccount(self):
        expmsg="Invalid email address"
        actmsg = str(self.driver.find_element_by_xpath(LocatorAddress.errmsg_invalid_email_xpath).text)
        bobj.verifyText(actmsg, expmsg)

    def verifyInvalidEmailAdderess(self):
        expmsg="Invalid email address"
        actmsg = str(self.driver.find_element_by_xpath(LocatorAddress.errmsg_invalid_email_xpath).text)
        bobj.verifyText(actmsg, expmsg)








