import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # login
        wd = self.app.wd
        self.app.open_home_page()
        time.sleep(1)
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("username").click()
        wd.find_element_by_xpath(u"//input[@value='Вход']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Вход']").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logget_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logget_user() == username

    def get_logget_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.user-info").text

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.user-info").click()
        self.app.lgout_page()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logget_in():
            self.logout()

    def is_logget_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0




