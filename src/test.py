


# #!/usr/bin/env python
# #coding=utf-8

# from aliyunsdkcore.client import AcsClient
# from aliyunsdkcore.acs_exception.exceptions import ClientException
# from aliyunsdkcore.acs_exception.exceptions import ServerException
# from aliyunsdkcore.auth.credentials import AccessKeyCredential
# from aliyunsdkcore.auth.credentials import StsTokenCredential
# from aliyunsdkcdn.request.v20180510.DescribeCdnDomainConfigsRequest import DescribeCdnDomainConfigsRequest

# credentials = AccessKeyCredential('<your-access-key-id>', '<your-access-key-secret>')
# # use STS Token
# # credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>', '<your-sts-token>')
# client = AcsClient(region_id='cn-shenzhen', credential=credentials)

# request = DescribeCdnDomainConfigsRequest()
# request.set_accept_format('json')

# request.set_DomainName("download.visionwx.com")
# request.set_FunctionNames("host_redirect")
# # request.set_ConfigId("43")

# response = client.do_action_with_exception(request)
# # python2:  print(response) 
# print(str(response, encoding='utf-8'))


# # -*- coding: utf-8 -*-
# # This file is auto-generated, don't edit it. Thanks.
# import sys

# from typing import List

# from alibabacloud_cdn20180510.client import Client as Cdn20180510Client
# from alibabacloud_tea_openapi import models as open_api_models
# from alibabacloud_cdn20180510 import models as cdn_20180510_models


# class Sample:
#     def __init__(self):
#         pass

#     @staticmethod
#     def create_client(
#         access_key_id: str,
#         access_key_secret: str,
#     ) -> Cdn20180510Client:
#         """
#         使用AK&SK初始化账号Client
#         @param access_key_id:
#         @param access_key_secret:
#         @return: Client
#         @throws Exception
#         """
#         config = open_api_models.Config(
#             # 您的AccessKey ID,
#             access_key_id=access_key_id,
#             # 您的AccessKey Secret,
#             access_key_secret=access_key_secret
#         )
#         # 访问的域名
#         config.endpoint = f'cdn.aliyuncs.com'
#         return Cdn20180510Client(config)

#     @staticmethod
#     def main(
#         args: List[str],
#     ) -> None:
#         client = Sample.create_client('<your-access-key-id>', '<your-access-key-secret>')
#         batch_set_cdn_domain_config_request = cdn_20180510_models.BatchSetCdnDomainConfigRequest(
#             domain_names='download.visionwx.com',
#             functions='[ { "functionArgs": [ { "argName": "regex", "argValue": "^/test/Boom_extension_latest.zip$" }, { "argName": "replacement", "argValue": "/boom_extension/test/boom_extension-2.1.1.4.zip" } ], "functionName": "host_redirect" , "configId": "209475701391360"} ]'
#         )
#         # 复制代码运行请自行打印 API 的返回值
#         client.batch_set_cdn_domain_config(batch_set_cdn_domain_config_request)

#     @staticmethod
#     async def main_async(
#         args: List[str],
#     ) -> None:
#         client = Sample.create_client('accessKeyId', 'accessKeySecret')
#         batch_set_cdn_domain_config_request = cdn_20180510_models.BatchSetCdnDomainConfigRequest(
#             domain_names='download.visionwx.com',
#             functions='[ { "functionArgs": [ { "argName": "regex", "argValue": "^/test/Boom_extension_latest.zip$" }, { "argName": "replacement", "argValue": "/boom_extension/test/boom_extension-2.1.1.4.zip" } ], "functionName": "host_redirect" , "configId": "209475701391360"} ]'
#         )
#         # 复制代码运行请自行打印 API 的返回值
#         await client.batch_set_cdn_domain_config_async(batch_set_cdn_domain_config_request)


# if __name__ == '__main__':
#     Sample.main(sys.argv[1:])
