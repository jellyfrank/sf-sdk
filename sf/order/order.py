#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm

QUERY_URL = "https://www.sf-express.com/we/ow/chn/sc/waybill/waybill-detail/"


class Order(Comm):

    def create_order(self, orderId, contactInfoList, cargoDetails, monthlyCard=None, expressTypeId=1, isReturnRoutelabel=1, **kwargs):
        """
        下订单接口

        param language:String(10) 必填 响应报文的语言， 缺省值为zh-CN，目前支持以下值zh-CN 表示中文简体， zh-TW或zh-HK或 zh-MO表示中文繁体， en表示英文
        param orderId: String(64) 客户订单号，不能重复
        param waybillNoInfoList: List		顺丰运单号
        param customsInfo: CustomsInfo 报关信息
        param cargoDetails: List 托寄物信息
        param cargoDesc: String(20) 拖寄物类型描述,如： 文件，电子产品，衣服等
        param extraInfoList: List 扩展属性
        param serviceList: List 增值服务信息，支持附录： 《增值服务产品表》
        param contactInfoList: List 收寄双方信息
        param monthlyCard: String(20): 条件 顺丰月结卡号 月结支付时传值，现结不需传值；沙箱联调可使用测试月结卡号7551234567（非正式，无须绑定，仅支持联调使用）
        param payMethod: Number(2): 1: 付款方式，支持以下值： 1:寄方付 2:收方付 3:第三方付
        param expressTypeId: Number(5): 1: 快件产品类别， 支持附录 《快件产品类别表》 的产品编码值，仅可使用与顺丰销售约定的快件产品
        param parcelQty: Number(5): 1: 包裹数，一个包裹对应一个运单号；若包裹数大于1，则返回一个母运单号和N-1个子运单号
        param totalLength: Number(16,5) 客户订单货物总长，单位厘米， 精确到小数点后3位， 包含子母件
        param totalWidth: Number(16,5) 客户订单货物总宽，单位厘米， 精确到小数点后3位， 包含子母件
        param totalHeight: Number(16,5) 客户订单货物总高，单位厘米， 精确到小数点后3位， 包含子母件
        param volume: Number(16,5) : 订单货物总体积，单位立方厘米, 精确到小数点后3位，会用于计抛 (是否计抛具体商务沟通中 双方约定)
        param totalWeight: Number(17,5): 条件 订单货物总重量（郑州空港海关必填）， 若为子母件必填， 单位千克， 精确到小数点后3位，如果提供此值， 必须>0 (子母件需>6)
        param totalNetWeight: Number(17,5) 商品总净重
        param sendStartTm: Date: 接收 到报 文的 时间: 要求上门取件开始时间， 格式： YYYY-MM-DD HH24:MM:SS， 示例： 2012-7-30 09:30:00 （预约单传预约截止时间，不赋值默认按当前时间下发，1小时内取件）
        param isDocall: Number(1): 0: 是否通过手持终端 通知顺丰收派 员上门收件，支持以下值： 1：要求 0：不要求
        param isSignBack: Number(1): 0: 是否返回签回单 （签单返还）的运单号， 支持以下值： 1：要求 0：不要求
        param custReferenceNo: String(100) 客户参考编码：如客户原始订单号
        param temperatureRange: Number(2): 条件 温度范围类型，当 express_type为12 医药温控件 时必填，支持以下值： 1:冷藏 3：冷冻
        param orderSource: String(50) 订单平台类型 （对于平台类客户， 如果需要在订单中 区分订单来源， 则可使用此字段） 天猫:tmall， 拼多多：pinduoduo， 京东 : jd 等平台类型编码
        param remark: String(100) 备注
        param isOneselfPickup: Number(1): 0: 快件自取，支持以下值： 1：客户同意快件自取 0：客户不同意快件自取
        param filterField: String 筛单特殊字段用来人工筛单
        param isReturnQRCode: Number(1): 0: 是否返回用来退货业务的 二维码URL， 支持以下值： 1：返回二维码 0：不返回二维码
        param specialDeliveryTypeCode: String(3) 特殊派送类型代码 1:身份验证
        param specialDeliveryValue: String(100) 特殊派件具体表述 证件类型: 证件后8位如： 1:09296231（1 表示身份证， 暂不支持其他证件）
        param merchantPayOrderNo: String(100) 商户支付订单号
        param isReturnSignBackRoute label: Number(1): 0: 是否返回签回单路由标签： 默认0， 1：返回路由标签， 0：不返回
        param isReturnRoutelabel: Number(1): 1: 是否返回路由标签： 默认1， 1：返回路由标签， 0：不返回；除部分特殊用户外，其余用户都默认返回
        param isUnifiedWaybillNo: Number(1): 0: 是否使用国家统一面单号 1：是， 0：否（默认）
        param podModelAddress: String(1024) 签单返还范本地址
        param inProcessWaybillNo: String(100) 头程运单号（郑州空港海关必填）
        param isGenWaybillNo: Number(1)	1	是否需求分配运单号1：分配 0：不分配（若带单号下单，请传值0）

        return: dict 接口返回结果
                success: true/false 接口调用是否成功
                errorCode: 错误码
                errorMsg: 错误信息
                msgData: 成功后返回的数据
        """
        data = {
            "language": kwargs.get("language",None) or self._language,
            "orderId": orderId,
            "contactInfoList": [c.to_dict() for c in contactInfoList],
            "cargoDetails": [c.to_dict() for c in cargoDetails],
            "monthlyCard": monthlyCard,
            "expressTypeId": expressTypeId,
            "isReturnRoutelabel": isReturnRoutelabel,
        }

        data.update(kwargs)
        return self.post("EXP_RECE_CREATE_ORDER", data)

    def confirm_order(self, orderId, dealType=1, **kwargs):
        """
        订单确认/取消接口-速运类API

        param: orderId	String(64)	是		客户订单号
        param: dealType	Number(1)	否	1	客户订单操作标识: 1:确认 (丰桥下订单接口默认自动确认，不需客户重复确认，该操作用在其它非自动确认的场景) 2:取消
        param: waybillNoInfoList	List	否		顺丰运单号(如dealtype=1， 必填)
        param: customsBatchs	String(20)	否		报关批次
        param: collectEmpCode	String(30)	否		揽收员工号
        param: inProcessWaybillNo	String(100)	否		头程运单号
        param: sourceZoneCode	String(10)	否		原寄地网点代码
        param: destZoneCode	String(10)	否		目的地网点代码
        param: totalWeight	Number(17,5)	否		订单货物总重量，包含子母 件，单位千克，精确到小数点 后3位，如果提供此值，必 须>0
        param: totalVolume	Number(16,5)	否		订单货物总体积，单位立方厘 米，精确到小数点后3位，会 用于计抛（是否计抛具体商务 沟通中双方约定）
        param: expressTypeId	Number(5)	否		快件产品类别，支持附录《快 件产品类别表》的产品编码 值，仅可使用与顺丰销售约定 的快件产品
        param: extraInfoList	List	否		扩展属性
        param: totalLength	Number(16, 5)	否		客户订单货物总长，单位厘米， 精确到小数点后3位，包含子 母件
        param: totalWidth	Number(16, 5)	否		客户订单货物总宽，单位厘米， 精确到小数点后3位，包含子 母件
        param: totalHeight	Number(16, 5)	否		客户订单货物总高，单位厘米， 精确到小数点后3位，包含子 母件
        param: serviceList	List	否		增值服务信息
        param: isConfirmNew	Number (1)	否		是否走新通用确认1：支持修改联系人 2：支持改其他客户订单默认0
        param: destContactInfo	OrderContactInfoDto	否		收件人信息
        param: isDocall	Number(1)	否		是否通过手持终端通知顺丰收派员上门收件， 支持以下值：1：要求其它为不要求
        param: specialDeliveryTypeCode	String(3)	否		1. 特殊派送类型代码 身份验证 2. 极效前置单
        param: specialDeliveryValue	String(100)	否		1> 特殊派件具体表述 证件类型:证件后8位 如：1:09296231（1表示身份证，暂不支持其他证件） 2>.极效前置单时:Y:若不支持则返回普通运单N:若不支持则返回错误码
        param: sendStartTm	Date	否		预约时间(上门揽收时间)
        param: pickupAppointEndtime	Date	否		上门揽收截止时间
        """
        data = {
            "orderId": orderId,
            "dealType": dealType
        }

        data.update(kwargs)
        return self.post("EXP_RECE_UPDATE_ORDER", data)

    def get_order(self, orderId, searchType='1', language=None):
        """
        订单结果查询接口

        params：
        orderId	String(64)	是		客户订单号
        searchType	String(10)	否		查询类型：1正向单 2退货单
        language	String(10)	否		响应报文的语言， 缺省值为zh-CN，目前支持以下值zh-CN 表示中文简体， zh-TW或zh-HK或 zh-MO表示中文繁体， en表示英文
        """
        data = {
            "language": language or self._language,
            "orderId": orderId,
            "searchType": searchType,
            "language": language
        }

        return self.post("EXP_RECE_SEARCH_ORDER_RESP", data)

    def get_route_info(self, trackingNumber, trackingType=1, methodType=1, referenceNumber=None, checkPhoneNo=None, language=None):
        """
        路由查询接口接口-速运类API

        param trackingNumber: 查询号: trackingType=1,则此值为顺丰运单号 如果trackingType=2,则此值为客户订单号
        param trackingType: 查询号类别: 1:根据顺丰运单号查询,trackingNumber将被当作顺丰运单号处理 2:根据客户订单号查询,trackingNumber将被当作客户订单号处理
        param methodType: 路由查询类别: 1:标准路由查询 2:定制路由查询
        param referenceNumber: 参考编码(目前针对亚马逊客户,由客户传)
        param checkPhoneNo: 校验电话号码后四位值;

        return: 包含节点信息的路由
        """
        data = {
            "language": language or self._language,
            "trackingNumber": trackingNumber,
            "trackingType": trackingType,
            "methodType": methodType,
            "referenceNumber": referenceNumber,
            "checkPhoneNo": checkPhoneNo
        }

        return self.post("EXP_RECE_SEARCH_ROUTES", data)

    def can_delivery(self, orderId, monthlyCard=None, filterType=1, contactInfos=None):
        """
        订单筛选接口-速运类API

        客户系统通过此接口向顺丰系统发送主动的筛单请求,用于判断客户的收、派地址是否属于顺丰的收派范围。

        param orderId: String 到件方详细地址,需要包括省市区
        param orderid: String 客户订单号,filter_type=2则必须提供
        param filterType: Int 筛单类别: 1:自动筛单(系统根据地址库进行判断,并返回结果,系统无法检索到可派送的将返回不可派送) 2:可人工筛单(系统首先根据地址库判断,如果无法自动判断是否收派,系统将生成需要人工判断的任务,后续由人工处理,处理结束后,顺丰可主动推送给客户系统)
        param contactInfos: List 地址信息
        """

        data = {
            "orderId": orderId,
            "monthlyCard": monthlyCard,
            "filterType": filterType,
            "contactInfos": contactInfos
        }

        return self.post("EXP_RECE_FILTER_ORDER_BSP", data)

    
    def query_delivery(self, businessType,destAddress,srcAddress, weight=None,volume=None,consignedTime=None,searchPrice=0):
        """
        时效标准及价格查询接口-速运类API

        客户可通过接口查询从特定原寄地寄特定目的地的时效和价格。

        param businessType: 快件产品：可以为空，为空时查询默认时效对应的产品列表。不为空时以数字代码业务类型，例如：1：表示“”2：表示“顺丰特惠”5：表示“顺丰次晨”6：表示“即日件
        param destAddress: 目的地信息
        param srcAddress: 原寄地信息
        param weight: 货物总重量，包含子母件，单位千克，精确到小数点后2位，如果提供此值，必须>0
        param volume: 货物的体积（长、宽、高分别以厘米为单位计算体积），精确到小数点后2位。
        param consignedTime: 寄件时间，格式为YYYY-MM-DD HH24:MM:SS，示例2013-12-27 17:54:20。
        param searchPrice: 1：表示查询含价格的接口0：表示查询不含价格的接口 备注：限制只能为0,1或者不传searchPrice，不可以为空,null
        """

        data = {
            "businessType": businessType,
            "destAddress": destAddress.to_dict(),
            "srcAddress": srcAddress.to_dict(),
            "weight": weight,
            "volume": volume,
            "consignedTime": consignedTime,
            "searchPrice": searchPrice
        }

        return self.post("EXP_RECE_QUERY_DELIVERTM", data)
