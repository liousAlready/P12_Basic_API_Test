# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 11:07 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : common_api.py
# @Software: PyCharm


import requests
from common.localconfig_utlis import local_config


def get_access_token_api(session, grant_type, appid, secret):
    url = local_config.URL + '/cgi-bin/token'
    params = {
        "grant_type": grant_type,
        "secret": secret,
        "appid": appid
    }
    response = session.get(url, params=params)
    return response


def get_access_token_value(session):
    response = get_access_token_api(session,
                                    "client_credential",
                                    local_config.APPID,
                                    local_config.SECRET)
    token_id = response.json()['access_token']
    return token_id


def create_usr_tag_api01(session, access_token, tag_json):  # 方式一：建议
    get_params = {"access_token": access_token}
    post_params = tag_json
    response = session.post(url=local_config.URL + '/cgi-bin/tags/create',
                            params=get_params,
                            json=post_params)
    return response


# def create_usr_tag_api02(session, access_token, tag):  # 方式二：表述不当
#     get_params = {"access_token": access_token}
#     post_params = {"tag": {"name": tag}}
#     response = session.post(url=local_config.URL + '/cgi-bin/tags/create',
#                             params=get_params,
#                             json=post_params)
#     return response


def deleter_usr_tag_api(session, access_token, tag_json):  # 方式二：表述不当
    get_params = {"access_token": access_token}
    post_params = tag_json
    response = session.post(url=local_config.URL + '/cgi-bin/tags/delete',
                            params=get_params,
                            json=post_params)
    return response
