# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_cdn20180510.client import Client as Cdn20180510Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cdn20180510 import models as cdn_20180510_models 
import os

# 获取环境变量
def getEnvPara(parameterName, default=None, 
    raiseExceptionIfNone=True):
    parameterValue = os.environ.get(parameterName, default)
    if parameterValue is None and raiseExceptionIfNone:
        raise Exception(parameterName + " not defined")
    return parameterValue

ACCESS_KEY_ID = getEnvPara(parameterName="ACCESS_KEY_ID")
ACCESS_KEY_SECRET = getEnvPara(parameterName="ACCESS_KEY_SECRET")
DOMAIN = getEnvPara(parameterName="DOMAIN")
REDIRECT_REGEX = getEnvPara(parameterName="REDIRECT_REGEX")
REDIRECT_REPLACEMENT = getEnvPara(parameterName="REDIRECT_REPLACEMENT")
REDIRECT_CONFIG_ID = getEnvPara(parameterName="REDIRECT_CONFIG_ID")

class Cdn:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Cdn20180510Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'cdn.aliyuncs.com'
        return Cdn20180510Client(config)
    
    @staticmethod
    def updateHostRedirect() -> None:
        client = Cdn.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        batch_set_cdn_domain_config_request = cdn_20180510_models.BatchSetCdnDomainConfigRequest(
            domain_names=DOMAIN,
            functions='[ { "functionArgs": [ { "argName": "regex", "argValue": "' + REDIRECT_REGEX + '" }, { "argName": "replacement", "argValue": "' + REDIRECT_REPLACEMENT + '" } ], "functionName": "host_redirect" , "configId": "' + REDIRECT_CONFIG_ID + '"} ]'
        )
        # 复制代码运行请自行打印 API 的返回值
        client.batch_set_cdn_domain_config(batch_set_cdn_domain_config_request)

if __name__ == '__main__':
    Cdn.updateHostRedirect()