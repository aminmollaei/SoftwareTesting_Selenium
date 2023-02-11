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
        self.driver.get('http://localhost:8080/')


    def first_test(self):
        print('Running Test#1')
        detailsTag = self.driver.find_element(By.XPATH, '/html/body/div/div/div/details')
        detailsTag.click()
        self.assertTrue(detailsTag.get_attribute('open') is not None)
        print('Test#1 passed successfully')

    def second_test(self):
        print('Running Test#2')
        nameLabel = self.driver.find_element(By.XPATH, '/html/body/div/div/h2')
        textField = self.driver.find_element(By.XPATH, '/html/body/div/div/input')
        textField.clear()
        targetValue = 'Johann_Sebastian_Bach'
        currentTarget = ''
        charactersValid = True
        for character in tqdm(targetValue): 
            textField.send_keys(character)
            currentTarget += character
            tmpLabel = nameLabel.text[12:]
            tmpLabel = tmpLabel[:-2]
            if tmpLabel != currentTarget:
                charactersValid = False
                break
            time.sleep(0.1)
        self.assertTrue(charactersValid)
        print('Test#2 passed successfully')
    
    def test(self):  
        time.sleep(1) 
        self.first_test()
        self.second_test() 

    def tearDown(self):
        dummy = input()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
