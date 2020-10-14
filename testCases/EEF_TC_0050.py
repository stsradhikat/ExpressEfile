import unittest
import HtmlTestRunner
import sys
import random

from PageObjects.Pages.SignInPage import SignInPage
from Parent.SeleniumBase import Base
from PageObjects.Pages.HomePage import HomePage
sys.path.append("D:/Python Projects/ExpressEfile/")
global bobj
bobj= Base()

#***   Verify sign in with already exisiting Facebook ID  ***#

class SignInTest(unittest.TestCase,Base,SignInPage):



    @classmethod
    def setUpClass(cls):
        bobj.startApp()

    def test_signin(self):


            spobj=SignInPage(self.driver)
            spobj.clickSignIn()
            spobj.setEmailAddress(bobj.readExcel("Sign_In_Test_Data",3,2))
            spobj.setPassword(bobj.readExcel("Sign_In_Test_Data",3,3))
            spobj.clickPopUpSignIn()
            spobj.verifyFacebookSignInAccount()






    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("completed")


if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Python Projects/ExpressEfile/Reports'))



