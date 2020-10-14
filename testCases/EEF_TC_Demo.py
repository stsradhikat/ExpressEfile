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


class SignInTest(unittest.TestCase,Base,SignInPage):



    @classmethod
    def setUpClass(cls):
        bobj.startApp()





    def test_signin(self):


            spobj=SignInPage(self.driver)
            spobj.clickSignIn()
            spobj.setEmailAddress(bobj.readExcel("SignIn",2,1))
          #  spobj.setEmailAddress("radhika.n@expressexcise.com")

            spobj.setPassword(bobj.readExcel("SignIn",2,2))
           # spobj.setPassword("Span@123")

            spobj.clickPopUpSignIn()
            homeobj = HomePage(self.driver)
            homeobj.verifySignIn()






    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        print("completed")


if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Python Projects/ExpressEfile/Reports'))



