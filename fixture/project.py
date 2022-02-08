from selenium.webdriver.support.ui import Select
from model.project import Project
import re
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

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        #wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def select_contact_by_select_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='%s']" % id).click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        #wd.find_elements_by_name("selected[]")[index].click()
        #s_id = "input[value='%s']" % id
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def select_first_contacts(self):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]").click()

    def count_project(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # fill form
        self.fill_contact(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # fill form
        self.fill_contact(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def fill_name_project(self, project):
        wd = self.app.wd
        self.change_field_project("project-name", project.name)

    def change_field_project(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

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

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id = id, address=address, email=email, email2=email2, email3=email3,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def del_contact_by_id_in_group(self, id, id_group):
        wd = self.app.wd
        self.app.open_home_page()
        # тут посмотреть название крутежка
        wd.find_element_by_name("group").click()
        # тут выбор группы по id
        Select(wd.find_element_by_name("group")).select_by_value(id_group)
        # выбор контакта
        self.select_contact_by_select_id(id)
        wd.find_element_by_name("remove").click()
        self.contact_cache = None

    def select_group_by_select_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='%s']" % id).click()










