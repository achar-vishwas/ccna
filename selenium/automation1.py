import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FloatingMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver=webdriver.Chrome()
        driver.get("https://www.marutisuzuki.com/")
        print(driver.title)
    @classmethod
    def tearDownClass(cls):
        print("Testing finished")


    @classmethod
    def setUp(self):
       self.driver=webdriver.Chrome()
       self.driver.get("https://www.marutisuzuki.com/") #navigate maruthi suzuki website
       self.driver.find_element(By.XPATH, "//a[@class='floatingIcon']").click()  #clicking on floating menu
       self.driver.find_element(By.ID,"book-a-showroom").click()  #clicking on show room visit inside floating menu
       time.sleep(1)


    def test1_name_email(self):
        self.driver.find_element(By.ID,"bttfname").send_keys("Arunsagar")
        self.driver.find_element(By.ID, "newTestEmail").send_keys("arun@gmail.com")
        time.sleep(2)
        self.driver.close()


    def test2_state_city(self):
        drop_down1 = self.driver.find_element(By.ID, "dealerstate")
        drop_down1.find_element(By.XPATH, "//option[@value='KT']").click()
        time.sleep(2)
        self.driver.close()


if __name__=="__main__":
    unittest.main()
