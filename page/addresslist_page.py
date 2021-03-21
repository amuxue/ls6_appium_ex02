#点击添加成员
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.memberinvite_page import MemberInvitePage


class AddressListPage(BasePage):
    def add_member(self):
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)