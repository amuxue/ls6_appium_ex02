import pytest

from page.app import App
import yaml

def get_data():
    with open('../data/data.yml',encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        return data

class TestContact:
    def setup(self):
        self.app=App()
        self.main=self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,phonenum",get_data()['add'])
    def test_add_contact(self,name,phonenum):
        # name='zhangsan1'
        # gender='男'
        # phonenum='12233331111'
        toast=self.main.add_member().addconnect_menual().edit_name(name).\
            edit_phonenum(phonenum).click_save().get_toast()
        assert toast=="添加成功"