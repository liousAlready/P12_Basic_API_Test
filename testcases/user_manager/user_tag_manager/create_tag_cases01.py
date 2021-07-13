# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 3:58 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : create_tag_cases.py
# @Software: PyCharm

import requests
import unittest
from common.localconfig_utlis import local_config
from common.log_utils import logger
from common.common_api import *


class CreateTagCase(unittest.TestCase):

    def setUp(self) -> None:
        self.host = local_config.URL
        self.session = requests.Session()

    def tearDown(self) -> None:
        pass

    def test_add_tag(self):  # 提供测试数据  测试的操作步骤 断言判定
        logger.info("[case03] 成功创建用户标签")
        token_id = get_access_token_value(self.session)  # 取token
        post_params = {"tag": {"name": "zxasqw12313"}}  # 传参
        creat_tags_response = create_usr_tag_api01(self.session, token_id, post_params)
        actual_value = creat_tags_response.json()['tag']['name']
        self.assertEqual(actual_value, "zxasqw12313")


if __name__ == "__main__":
    unittest.main()
