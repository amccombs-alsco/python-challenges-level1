import time
from Framework.screenshot import Screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest


class Copart7(unittest.TestCase):
    def setUp(self):
        # This section will get the copart website and maximize the window.
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.get('https://www.copart.com')
        assert'Auto Auction', self.driver.title
        self.driver.maximize_window()
        driver = self.driver
        self.s = Screenshot(driver, 'Oops')

    def find_make_and_model(self):
        div = 1
        count = 1
        while div < 5:
            num = 1
            while num < 6:
                cars = '//*[@id="tabTrending"]/div[1]/div[2]/div[' + str(div) + ']/ul/li[' + str(num) + ']'
                wait = WebDriverWait(self.driver, 200)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabTrending"]')))
                for c in self.driver.find_elements_by_xpath(cars):
                    c.click()
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="serverSideDataTable"]/tbody')))
                search = '//span[text() = "Search Results"]'
                time.sleep(1)
                if EC.text_to_be_present_in_element(search, 'Search Results'):
                    print('Page', count, 'verified')
                    count += 1
                else:
                    self.s.screen_shot_name()
                self.driver.back()
                self.driver.back()
                time.sleep(1)

                num += 1
            div += 1

    def test_urls(self):
        self.find_make_and_model()

    def tear_down(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()





