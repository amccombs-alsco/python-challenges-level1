import unittest
from selenium import webdriver


class PopularItems(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.get('https://www.copart.com')
        assert 'Auto Auction', self.driver.title
        self.driver.maximize_window()
    # This function will get a list of cars from the copart most popular items makes/models section on the homepage

    def test_get_cars(self):
        cars = self.driver.find_elements_by_xpath('//div[@class = "row"]//li[contains(@ng-repeat, "popularSearch")]//a')
        i = 0
        while i in range(len(cars)):
            for car in cars:
                car_url = car.get_attribute('href')
                print(car.text, '-', car_url)
                i += 1

    def tear_down(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()



