from selenium import webdriver
from TestURL.EnvironmentURL import EnvUrl
import random
import openpyexcel


class Base():


    driver = webdriver.Chrome(executable_path="D://Python Projects//test//Drivers//chromedriver85.exe")
    global baseurl
    baseurl = EnvUrl.SprintUrl
    # For taking Screen shots
    def capture(self,name):
        try:
            self.driver.save_screenshot("D://Python Projects//ExpressEfile//Images//"+name+".png")
        except Exception as ex:
            print("Screenshot not captured"+str(ex))
            self.capture("Error"+str(random.random()))

    #For launching browser
    def startApp(self):
        try:
            self.driver.get(baseurl)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
        except Exception as ex:
            print("Browser could not be launched"+str(ex))
            self.capture("Error"+str(random.random()))

    #For reading from excel sheet
    def readExcel(self,sheetname,rowno,colno):
        try:
            workbook=openpyexcel.load_workbook("D:/Python Projects/ExpressEfile/Data/ExpressEfileDataProvider.xlsx")
            sheet=workbook.get_sheet_by_name(sheetname)
            value=sheet.cell(row=rowno,column=colno).value
            return str(value)

        except Exception as ex:
            print("Can not read excel data" + str(ex))
            self.capture("Error"+str(random.random()))

    # For webdriver wait
    def wait(self):
        self.driver.implicitlyWait(10)
    # For text comparison
    def verifyText(self,actaultext,expectedtext):

            assert actaultext==expectedtext






        





