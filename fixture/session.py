

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_xpath("//input[@value='Войти']").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Войти']").click()

    def open_home_page(self):
        driver = self.app.driver
        driver.get(self.app.base_url)

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//span[@text='administrator']").click()
        driver.find_element_by_link_text("/mantisbt-2.24.3/logout_page.php").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        print(len(driver.find_elements_by_xpass("//*[@id='breadcrumbs']/ul/li/a")))
        return len(driver.find_elements_by_xpass("//*[@id='breadcrumbs']/ul/li/a")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return self.get_logged_user() == username

    def get_logged_user(self):
        driver = self.app.driver
        return driver.driver.find_elements_by_xpass("//*[@id='breadcrumbs']/ul/li/a").text
