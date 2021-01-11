from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from fixture.session import SessionHelper
from fixture.soap_helper import SoapHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="D:\Pithon\Python_Mantis_Test\Drivers\chromedriver.exe")
        self.driver.implicitly_wait(1) # waiting in seconds
        self.base_url = "http://localhost/mantisbt-2.24.3/"
        self.session = SessionHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def adapted_url_to_webdriver(self, local_driver_url):
        wd_url = __file__
        wd_url = wd_url.strip("fixture\\application.py")
        wd_url = "\\".join([wd_url, local_driver_url])
        return wd_url