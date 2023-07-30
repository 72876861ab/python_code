# coding: utf-8
# 我是谁
import os
from string import Template
import jsonpath, pytest, requests
from xToolkit import xfile
from day000.day002.global_value import g_var

测试数据 = xfile.read("D:\pythonProject\day000\day002\模拟测试用例.xls").excel_to_dict(sheet=1)
# print(测试数据)
@pytest.mark.parametrize("case_info", 测试数据)
def test_case_exec(case_info):
    url = case_info["接口URL"]
    if "$" in url:
        url = Template(url).substitute(g_var().show_dict())
        # print(url)
    rs = requests.request(url=url,
                          params=eval(case_info["URL参数"]),
                          data=eval(case_info["JSON参数"]),
                          method=(case_info["请求方式"]))
    if case_info["提取参数"]:
        ltoken = jsonpath.jsonpath(rs.json(),"$.."+case_info["提取参数"])
        g_var().set_dict(case_info["提取参数"], ltoken[0])

        # assert rs.status_code == case_info["预期状态码"]
        # assert rs.json()[case_info["预期返回内容"]] == 0
if __name__ == '__main__':
    pytest.main(["-vs",
                 "--capture=sys",
                 "Test_apiframework.py",
                 "--clean-alluredir","--alluredir=allure-results"])

os.system("allure generate ./allure-results/ -o ./report_allure --clean")

