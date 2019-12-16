import unittest
from selenium import webdriver
from Framework.Filters import Filters
from Framework.Search import Searches
from Framework.screenshot import Screenshot


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.get('https://www.copart.com')
        assert 'Auto Auction', self.driver.title
        self.driver.maximize_window()

    def test_search_car_negative(self):
        driver = self.driver
        search = Searches(driver)
        filter = Filters(driver)
        search.find_car('honda')
        filter.choosing_side_menu_filter('Model', 'skyline')

    def test_search_car_positive(self):
        driver = self.driver
        search = Searches(driver)
        filter = Filters(driver)
        search.find_car('nissan')
        filter.choosing_side_menu_filter('Model', 'skyline')

    def test_view_screenshot(self):
        driver = self.driver
        screenshootin = Screenshot(driver, 'No_Filter')
        screenshootin.open_screenshot()

    if __name__ == '__main__':
        unittest.main()









# go to site
# search for nissan with model of skyline
# take screenshot upon getting exception