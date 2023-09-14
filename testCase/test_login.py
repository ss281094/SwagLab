from pageObject.LoginPage import SwagLab_Login
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig


class Test_Login:
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()
    log = LogGenerator.loggen()

    def test_page_title_001(self, setup):
        self.log.info("Testcase test_page_title_001 is started")
        self.log.info("Opening browser")
        self.driver = setup       #open browser & URL
        self.log.info("Page Title is " + self.driver.title)
        if self.driver.title == "Swag Labs":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("D:\\python project\\swagLab\\Screenshots\\test_page_title_001_Pass.png")
            self.log.info("Testcase test_page_title_001 is passed")
            assert True

        else:
            self.driver.save_screenshot("D:\\python project\\swagLab\\Screenshots\\test_page_title_001_Fail.png")
            self.log.info("Testcase test_page_title_001 is failed")
            assert False
        self.log.info("Testcase test_page_title_001 is completed\n")


    def test_login_002(self, setup):
        self.log.info("Testcase test_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lp = SwagLab_Login(self.driver)
        self.log.info("Entering Username")
        self.lp.Enter_Username("problem_user")
        self.log.info("Entering password :" )
        self.lp.Enter_Password("secret_sauce")
        self.log.info("Clicking in login button :")
        self.lp.Click_Login()
        self.log.info("Checking login status")
        if self.lp.Login_Status() == True:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("D:\\python project\\swagLab\\Screenshots\\test_login_002_Pass.png")
            self.log.info("Clicking on Menu button")
            self.lp.Click_Menu()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout()
            self.log.info("Testcase test_login_002 is passed")
            assert True
        else:
            self.driver.save_screenshot("D:\\python project\\swagLab\\Screenshots\\test_login_002_Fail.png")
            self.log.info("Testcase test_login_002 is failed")
            assert False
        self.log.info("Testcase test_login_002 is completed\n")




