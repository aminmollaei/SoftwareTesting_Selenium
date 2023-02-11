import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time

class SampleTeseCase(unittest.TestCase):
    def setUp(self):
         # open Firefox browser
        self.driver = webdriver.Firefox()
        # set window size
        self.driver.set_window_rect(0, 0, 1540, 550)
        # delete the cookies
        self.driver.delete_all_cookies()
        # navigate to the url
        self.driver.get('https://ahfarmer.github.io/calculator/')


    def test_add(self):
        print('Running Test_Add')

        # 925
        self.numbers[9].click()
        self.numbers[2].click()
        self.numbers[5].click()

        self.add.click()

        # 186
        self.numbers[1].click()
        self.numbers[8].click()
        self.numbers[6].click()

        self.equal.click()
        
        self.assertTrue(self.result.text == '1111')
        print('Test_Add passed successfully')
       

    def test_subtract(self):
        print('Running Test_Subtract')
        
        # 10
        self.numbers[1].click()
        self.numbers[0].click()

        self.subtract.click()

        # 25
        self.numbers[2].click()
        self.numbers[5].click()

        self.equal.click()
        
        self.assertTrue(self.result.text == '-15')
        print('Test_Subtract passed successfully')


    def test_multiply(self):
        print('Running Test_Multiply')

        # 14
        self.numbers[1].click()
        self.numbers[4].click()

        self.multiply.click()

        # 2
        self.numbers[2].click()

        self.equal.click()
        
        self.assertTrue(self.result.text == '28')
        print('Test_Multiply passed successfully')

    
    def test_divide(self):
        print('Running Test_Divide')

        # 200
        self.numbers[2].click()
        self.numbers[0].click()
        self.numbers[0].click()

        self.divide.click()

        # 4
        self.numbers[4].click()

        self.equal.click()
        
        self.assertTrue(self.result.text == '50')
        print('Test_Divide passed successfully')



    def test_decimal(self):
        print('Running Test_Decimal')

        # 6
        self.numbers[6].click()

        self.divide.click()

        self.numbers[1].click()
        self.numbers[0].click()

        self.add.click()

        # 6.5
        self.numbers[6].click()
        self.decimal.click()
        self.numbers[5].click()

        self.equal.click()

        self.assertTrue(self.result.text == '7.1')
        print('Test_Decimal passed successfully')
    
    def test(self):  
        self.result = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div') 
        self.numbers = [
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[5]/div[1]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div[1]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div[2]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div[3]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div[1]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div[2]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div[3]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/button'),
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/button')
        ]
        self.divide = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[4]/button')
        self.multiply = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[4]/button')
        self.subtract = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div[4]/button')
        self.add = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div[4]/button')
        self.equal = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[5]/div[3]/button')
        self.decimal = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button')

        self.test_add()
        self.test_subtract()
        self.test_multiply()
        self.test_divide()
        self.test_decimal()
        

    def tearDown(self):
        dummy = input()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
