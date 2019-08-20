# coding:utf-8
import unittest
from case.api_method import TestLogin
from case import HTMLTestRunner


class Runmain():
    def __init__(self):
        pass

    def run_case(self):
        suite=unittest.TestSuite()
        suite.addTests(map(TestLogin, ["test_01"]))
        st=open('report.html', 'wb')
        HTMLTestRunner.HTMLTestRunner(stream=st, title=u'接口自动化测试报告', description=u'测试者：Mr cai').run(suite)


if __name__ == '__main__':
    run=Runmain()
    run.run_case()
