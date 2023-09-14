from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Add_Cart:
    Click_Addcart_XPATH = (By.XPATH,"//div[@class='inventory_list']//div[1]//div[3]//button[1]" )
    Click_Shop_XPATH = (By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']//*[name()='svg']")
    Click_Checkout_XPATH = (By.XPATH,"//a[@class='btn_action checkout_button']")
    Text_FirstName_XPATH = (By.XPATH,"//input[@id='first-name']")
    Text_LastName_XPATH = (By.XPATH,"//input[@id='last-name']")
    Text_Zip_XPATH = (By.XPATH,"//input[@id='postal-code']")
    Click_Continue_XPATH = (By.XPATH,"//input[@value='CONTINUE']")
    Click_Finish_XPATH = (By.XPATH,"//a[@class='btn_action cart_button']")
    Click_FS_XPATH  = (By.XPATH,"//img[@class='pony_express']")
    Successmsg_XPATH = (By.XPATH,"//h2[@class='complete-header']")


    def __init__(self, driver):
        self.driver = driver

    def Click_Addcart(self):
        self.driver.find_element(*Add_Cart.Click_Addcart_XPATH).click()

    def Click_shop(self):
        self.driver.find_element(*Add_Cart.Click_Shop_XPATH).click()

    def Click_Checkout(self):
        self.driver.find_element(*Add_Cart.Click_Checkout_XPATH).click()

    def Enter_FirstName(self):
        self.driver.find_element(*Add_Cart.Text_FirstName_XPATH).send_keys("ABC")

    def Enter_LastName(self):
        self.driver.find_element(*Add_Cart.Text_LastName_XPATH).send_keys("xyz")

    def Enter_ZIP(self):
        self.driver.find_element(*Add_Cart.Text_Zip_XPATH).send_keys("458585")

    def Click_Continue(self):
        self.driver.find_element(*Add_Cart.Click_Continue_XPATH).click()

    def Click_Finish(self):
        self.driver.find_element(*Add_Cart.Click_Finish_XPATH).click()

    def Successmessage(self):
        try:
            success_message = self.driver.find_element(*Add_Cart.Successmsg_XPATH)
            return True
        except NoSuchElementException:
            return False


