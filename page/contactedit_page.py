#编辑成员的信息
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class ContactEditPage(BasePage):
    def edit_name(self,name):
        self.find((MobileBy.ID,"com.tencent.wework:id/b7m")).send_keys(name)
        return self
    def edit_gender(self,gender):
        # 显示等待
        locator=(MobileBy.XPATH,'//*[@text="男"]')
        ele=WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        if gender == '男':
            self.find_and_click((MobileBy.XPATH, '//*[@text="男"]'))
        else:
            self.find_and_click((MobileBy.XPATH, '//*[@text="女"]'))
        return self

    def edit_phonenum(self,phonenum):
        self.find((MobileBy.ID,"com.tencent.wework:id/fwi")).send_keys(phonenum)
        return self

    def click_save(self):
        from page.memberinvite_page import MemberInvitePage
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/aj_"))
        return MemberInvitePage(self.driver)
