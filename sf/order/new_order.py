#!/usr/bin/python3
# @Time    : 2020-10-27
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm, Service


class NewOrder(Comm):

    @Service("EXP_RECE_CREATE_ORDER")
    def create_order(self, orderId, cargoDetails, contactInfoList,
                     language="zh-CN", waybillNoInfoList=None, customsInfo=None, cargoDesc=None,
                     extraInfoList=None, serviceList=None, monthlyCard=None, payMethod=1,
                     expressTypeId=1, parcelQty=1, totalLength=None, totalWidth=None,
                     totalHeight=None, volume=None, totalWeight=None, totalNetWeight=None,
                     sendStartTm=None, isDocall=0, isSignBack=0, custReferenceNo=None,
                     temperatureRange=None, orderSource=None, bizTemplateCode=None, remark=None,
                     isOneselfPickup=0, filterField=None, isReturnQRCode=0, specialDeliveryTypeCode=None,
                     specialDeliveryValue=None, realnameNum=None, merchantPayOrderNo=None, isReturnSignBackRoutelabel=0,
                     isReturnRoutelabel=0, isUnifiedWaybillNo=0, podModelAddress=None, collectEmpCode=None,
                     inProcessWaybillNo=None):
        """
        下订单接口
        params:
        orderId: 客户订单号
        cargoDetails: 托寄物信息 List
        contactInfoList: 收寄双方信息 List

        language: 响应报文的语言，缺省值为zh-CN
        waybillNoInfoList： 顺丰运单号 List
        customsInfo: 报关信息
        cargoDesc： 拖寄物类型描述,如：文件，电子产品，衣服等
        extraInfoList: 拓展属性 List
        serviceList: 增值服务信息 List
        payMethod: 付款方式，支持以下值：1:寄方付 2:收方付 3:第三方付
        expressTypeId: 快件产品类别
        parcelQty: 包裹数，一个包裹对应一个运单号；若包裹数大于1，则返回一个母运单号和N-1个子运单号
        totalLength: 客户订单货物总长，单位厘米，精确到小数点后3位，包含子母件
        totalWidth: 客户订单货物总宽，单位厘米，精确到小数点后3位，包含子母件
        totalHeight: 客户订单货物总高，单位厘米，精确到小数点后3位，包含子母件
        volume: 订单货物总体积，单位立方厘米,精确到小数点后3位，会用于计抛(是否计抛具体商务沟通中双方约定)
        totalWeight: 订单货物总重量，若为子母件必填，单位千克，精确到小数点后3位，如果提供此值，必须>0 (子母件需>6)
        totalNetWeight: 商品总净重
        sendStartTm: 要求上门取件开始时间，格式：YYYY-MM-DD HH24:MM:SS，示例：2012-7-30 09:30:00
        isDocall: 是否通过手持终端通知顺丰收派员上门收件，支持以下值：1：要求 0：不要求
        isSignBack: 是否返回签回单（签单返还）的运单号，支持以下值：1：要求 0：不要求
        custReferenceNo: 客户参考编码：如客户原始订单号
        temperatureRange: 温度范围类型，当press_type为12药温控件必填，支持以下值：冷藏 3：冷冻
        orderSource: 订单平台类型（对于平台类客户，如果需要在订单中区分订单来源，则可使用此字段） 天猫:tmall，拼多多：pinduoduo，京东 : jd等平台类型编码
        bizTemplateCode: 业务配置代码，业务配置代码指BSP针对客户业务需求配置的一套接口处理逻辑，一个接入编码可对应多个业务配置代码
        remark: 备注
        isOneselfPickup: 快件自取，支持以下值： 1：客户同意快件自取 0：客户不同意快件自取
        filterField: 筛单特殊字段 用来人工筛单
        isReturnQRCode: 是否返回用来退货业务的二维码URL，支持以下值：1：返回二维码 0：不返回二维码
        specialDeliveryTypeCode: 特殊派送类型代码1:身份验证
        specialDeliveryValue: 特殊派件具体表述证件类型:证件后8位如：1:09296231（1表示身份证，暂不支持其他证件
        realnameNum: 寄件实名认证流水号
        merchantPayOrderNo: 商户支付订单号
        isReturnSignBackRoutelabel: 是否返回签回单路由标签：默认0，1：返回路由标签，0：不返回
        isReturnRoutelabel: 是否返回路由标签：默认0，1：返回路由标签，0：不返回
        isUnifiedWaybillNo: 是否使用国家统一面单号 1：是， 0：否（默认）
        podModelAddress: 签单返还范本地址
        collectEmpCode: 揽收员工号
        inProcessWaybillNo: 头程运单号
        """
        pass
