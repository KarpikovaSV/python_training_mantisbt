from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from fixture.session import SessionHelper
from fixture.project import ProjectHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
        #self.wd = webdriver.Firefox()
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # Без задержки валятся тесты
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.get(self.base_url+"/manage_proj_page.php")

    def open_home_page_create(self):
        wd = self.wd
        if not wd.current_url.endswith("/manage_proj_create_page.php"):
            wd.get(self.base_url + "/manage_proj_create_page.php")

    # def open_page_edit(self):
    #     wd = self.wd
    #     if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("photo"))) > 0:
    #         #wd.get("http://localhost/addressbook/edit.php")
    #         bu = self.base_url
    #         wd.get(bu + "/edit.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def destroy(self):
        self.wd.quit()