#!/usr/bin/python3
# @Time    : 2022-12-04
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm
import requests


class Sheet(Comm):

    def print(self, templateCode, documents, version='2.0', fileType="pdf", sync=True, customTemplateCode=None, extJson=None):
        """
        云打印面单打印2.0接口-面单类API
        param templateCode:	模板编码	是	String	关联云打印接口后，点击查看，可在接口详情页获取模板编码，类似：fm_76130_standard_{partnerId}
        param documents:	业务数据	是	array	一批不要超过20个运单，字段定义参考 2.3.1 模板固定字段
        param version:	版本号	是	String	版本号，传固定值:2.0
        param fileType:	生成面单文件格式	否	String	pdf格式
        param sync:	是否同步	条件	boolean	true: 同步,false: 异步,默认同步
        param customTemplateCode:	自定义模板编码，当需要使用模板编辑器编辑自定义区时，将自定义模板编码赋值该字段	否	String	自定义模板必须是已发布的，且规格要和需要打印的模板对应
        param extJson:	扩展字段	否	Json	字段定义参考下方extJson字段

        """

        data = {
            "templateCode": templateCode,
            "documents": documents,
            "version": version,
            "fileType": fileType,
            "sync": sync,
            "customTemplateCode": customTemplateCode,
            "extJson": extJson
        }

        return self.post("COM_RECE_CLOUD_PRINT_WAYBILLS", data)

    def sync_print(self, templateCode, documents):
        """同步获取电子面单"""
        res = self.print(templateCode, documents)
        files = []
        for file in res['obj']['files']:
            resp = requests.get(file['url'], headers={
                "X-Auth-token": file['token']
            })
            files.append(resp.content)
        return files

    def get_custom_templates(self, sellerUserId, type=1, standardTemplateCode=None,):
        """
        获取自定义面单编码

        param sellerUserId: isv商家在isv平台注册的账号
        param type: 	查询类型，（1：商家自定义模板）
        param standardTemplateCode: 标准模板code，取值查看 2.3.2，不传值时，则查询所有规格的
        """

        data = {
            "sellerUserId": sellerUserId,
            "type": type,
            "standardTemplateCode": standardTemplateCode
        }

        return self.post("COM_RECE_CLOUD_CUSTOMTEMPLATE_LIST", data)