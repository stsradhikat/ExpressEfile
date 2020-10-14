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

#***  Verify sign in with  more than one "@" symbol  ***#

class SignInTest(unittest.TestCase,Base,SignInPage):



    @classmethod
    def setUpClass(cls):
        bobj.startApp()

    def test_signin(self):


            spobj=SignInPage(self.driver)
            spobj.clickSignIn()
            spobj.setEmailAddress(bobj.readExcel("Sign_In_Test_Data",7,2))
            spobj.setPassword(bobj.readExcel("Sign_In_Test_Data",7,3))
            spobj.clickPopUpSignIn()
            spobj.verifyInvalidEmailAdderess()
    @classmethod
    def tearDownClass(cls):
        #cls.driver.close()
        print("completed")


if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Python Projects/ExpressEfile/Reports'))



