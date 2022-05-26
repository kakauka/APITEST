import unittest
import allure
from selenium import webdriver
import dop

class Testing(unittest.TestCase):
    def setUp(self):
        executable_path = "C:\Python37-32\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path)
        self.driver.get('http://XXXXXX')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)

    @allure.feature('Feature1')
    @allure.story('Story1')
    # Check first
    def test_is_button_1_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[7]", "1", self)
        dop.check_input_field("1", self, False)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()