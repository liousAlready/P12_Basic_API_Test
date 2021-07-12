# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 4:39 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : start_run.py
# @Software: PyCharm


import unittest
from common import HTMLTestReportCN
from common.localconfig_utlis import local_config


def get_all_case_suite():
    discover = unittest.defaultTestLoader.discover(
        start_dir='./testcases',
        pattern='*_cases.py',
        top_level_dir='./testcases'
    )

    all_cases_suite = unittest.TestSuite()
    all_cases_suite.addTest(discover)

    return all_cases_suite


report_dir = HTMLTestReportCN.ReportDirectory(local_config.REPORT_PATH)
report_dir.create_dir("API_TEST_")  # 设置报告名字
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')  # 报告路径
fp = open(report_path, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title="limusen测试线性脚本",
                                         tester="Li",
                                         description="study~~~")  # description 测试备注
runner.run(get_all_case_suite())
fp.close()
