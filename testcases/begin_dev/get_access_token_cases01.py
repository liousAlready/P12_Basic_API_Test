# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 3:56 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : get_access_token_cases.py
# @Software: PyCharm


import requests
import unittest
from common.localconfig_utlis import local_config
from common.log_utils import logger
from common.common_api import *

'''

代码模块化

'''


class GetAccessTokenCase(unittest.TestCase):

    def setUp(self) -> None:
        self.host = local_config.URL
        self.session = requests.Session()

    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        '''[case01] 正常获取access_token测试'''
        logger.info("[case01] 正常获取access_token测试")
        response = get_access_token_api(self.session,
                                        "client_credential",
                                        "wxb637f897f0bf1f0d",
                                        "501123d2d367b109a5cb9a9011d0f084")
        self.assertEqual(response.json()['expires_in'], 7200)

    def test_appid_error(self):
        self._testMethodDoc = "[case02] appid错误时测试"
        logger.info("[case02] appid错误时测试~~")
        response = get_access_token_api(self.session,
                                        "client_credential",
                                        "wxb637f897f0bf1f0d12",
                                        "501123d2d367b109a5cb9a9011d0f084")
        self.assertEqual(response.json()['errcode'], 40013)


if __name__ == "__main__":
    unittest.main()
