#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

import base64
from hashlib import md5
from lxml import etree
import inspect
from itertools import zip_longest
from functools import partial

import requests
import uuid
import time
from copy import copy
import json

URL = "https://bspgw.sf-express.com/std/service"
HKURL = "https://sfapi-hk.sf-express.com/std/service"
SANDBOXURL = "https://sfapi-sbox.sf-express.com/std/service"
TOKEN_URL = "https://sfapi.sf-express.com/oauth2/accessToken"
TOKEN_SANDBOXURL = "https://sfapi-sbox.sf-express.com/oauth2/accessToken"


class Comm(object):
    """封装公共请求"""

    def __get__(self, instance, owner):
        self._clientcode = instance.clientcode
        self._checkword = instance.checkword
        self._sandbox = instance.sandbox
        self._language = instance.language
        self.get_access_token()
        return self

    def get_access_token(self):
        """获取AccessToken"""
        url = f"{TOKEN_SANDBOXURL if self._sandbox else TOKEN_URL}?partnerID={self._clientcode}&secret={self._checkword}&grantType=password"
        res = requests.post(url, headers={
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8"
        }).json()
        if res['apiResultCode'] == "A1000":
            self._access_token = res['accessToken']
        else:
            raise Exception(
                f"getting access token error:{res['apiResultCode'],res['apiErrorMsg']}")
        return self._access_token

    def get_public_params(self):
        """获取公共参数"""
        data = {
            "partnerID": self._clientcode,
            "requestID": str(uuid.uuid4()),
            "timestamp": int(time.time()),
            "accessToken": self._access_token
        }
        return data

    def post(self, service, data):
        """
        提交请求

        param data: 数据结构
        """

        post_data = self.get_public_params()
        copy_data = copy(data)

        for key, value in copy_data.items():
            if value is None:
                data.pop(key)

        post_data.update({
            "serviceCode": service,
            "msgData": json.dumps(data)
        })

        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }

        url = SANDBOXURL if self._sandbox else URL
        res = requests.post(url, data=post_data, headers=headers).json()
        if res['apiResultCode'] != 'A1000':
            raise Exception(res['apiErrorMsg'])
        return json.loads(res['apiResultData'])
