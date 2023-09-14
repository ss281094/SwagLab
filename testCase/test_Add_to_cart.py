import time

from pageObject.Add_to_cart import Add_Cart
from pageObject.LoginPage import SwagLab_Login
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig


class Test_Login:
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()
    log = LogGenerator.loggen()


    def test_ATC_003(self, setup):
        self.log.info("Testcase test_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lp = SwagLab_Login(self.driver)
        self.log.info("Entering Username")
        self.lp.Enter_Username("problem_user")
        self.log.info("Entering password :")
        self.lp.Enter_Password("secret_sauce")
        self.log.info("Clicking in login button :")
        self.lp.Click_Login()
        self.ac = Add_Cart(self.driver)
        time.sleep(3)
        self.log.info("click on add cart")
        self.ac.Click_Addcart()
        time.sleep(3)

        self.log.info("click on shop button")
        self.ac.Click_shop()
        time.sleep(3)
        self.log.info("click on checkout")
        self.ac.Click_Checkout()
        time.sleep(3)
        self.log.info("Enter FirstName")
        self.ac.Enter_FirstName()
        time.sleep(3)
        self.log.info("Enter LastName")
        self.ac.Enter_LastName()
        time.sleep(3)
        self.log.info("Enter Zip")
        self.ac.Enter_ZIP()
        time.sleep(3)
        self.log.info("click on continue")
        self.ac.Click_Continue()
        time.sleep(3)
        self.log.info("click on finish")
        self.ac.Click_Finish()
        time.sleep(3)
        self.log.info("showing success message")
        if self.ac.Successmessage()==True:
            self.driver.save_screenshot("D:\\python project\\swagLab\\Screenshots\\success_pass.png")

            assert True
        else:
            self.driver.save_screenshot("D:\\python project\\swagLab\\Screenshots\\success_Fail.png")
            assert False
        self.log.info("click on menu button")
        self.lp.Click_Menu()
        time.sleep(3)

        self.log.info("Clicking on logout button")
        self.lp.Click_Logout()

















