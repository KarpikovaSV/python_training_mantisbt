from selenium.webdriver.support.ui import Select
from model.project import Project
import random
import string
import time
from selenium.webdriver.common.by import By


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        # fill form
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_name_project(project)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()
        self.contact_cache = None

    def random(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def select_project_by_name(self, name):
        wd = self.app.wd
        table = wd.find_element_by_css_selector("table.table-striped.table-bordered.table-condensed.table-hover")
        tbody = table.find_element(By.TAG_NAME, "tbody")
        for element in tbody.find_elements(By.TAG_NAME, "a"):
            if name == element.text:
                element.click()
                return

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_project_by_name(name)
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
        time.sleep(3)
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
        self.contact_cache = None

    def count_project(self):
        wd = self.app.wd
        self.app.open_home_page()
        table = wd.find_element_by_css_selector("table.table-striped.table-bordered.table-condensed.table-hover")
        tbody = table.find_element(By.TAG_NAME, "tbody")
        return len(tbody.find_elements(By.TAG_NAME, "a"))

    def fill_name_project(self, project):
        wd = self.app.wd
        self.change_field_project("project-name", project.name)

    def change_field_project(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

    def get_project_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            table = wd.find_element_by_css_selector("table.table-striped.table-bordered.table-condensed.table-hover")
            tbody = table.find_element(By.TAG_NAME, "tbody")
            for element in tbody.find_elements(By.TAG_NAME, "a"):
                name = element.text
                self.contact_cache.append(Project(name=name))
        return list(self.contact_cache)

    def select_xpa(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)








