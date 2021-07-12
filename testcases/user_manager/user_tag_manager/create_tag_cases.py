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


class CreateTagCase(unittest.TestCase):

    def setUp(self) -> None:
        self.host = local_config.URL
        self.session = requests.Session()

    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        logger.info("[case03] 成功创建用户标签")
        params = {
            "grant_type": "client_credential",
            "appid": "wxb637f897f0bf1f0d",
            "secret": "501123d2d367b109a5cb9a9011d0f084",
        }
        content = self.session.get(url=self.host + '/cgi-bin/token', params=params)
        token_id = content.json()['access_token']
        print(token_id)

        get_params = {"access_token": token_id}
        post_params = {"tag": {"name": "zxzxczxcqq"}}
        headers = {'content_type': 'application/json'}
        creat_tags_response = self.session.post(url=self.host + '/cgi-bin/tags/create', params=get_params,
                                                json=post_params,
                                                headers=headers)
        actual_value = creat_tags_response.json()['tag']['name']
        self.assertEqual(actual_value, "zxzxczxcqq")


if __name__ == "__main__":
    unittest.main()
