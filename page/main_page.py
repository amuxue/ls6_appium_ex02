# 点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from page.addresslist_page import AddressListPage
from page.base_page import BasePage


class MainPage(BasePage):
    def click_addresslist(self):
        self.find_and_click((MobileBy.XPATH,'//*[@text="通讯录"]'))
        return AddressListPage(self.driver)