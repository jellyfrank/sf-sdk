#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm, Service
import inspect


class Order(Comm):

    @Service("OrderService")
    def create_order(self, orderid, d_company, d_contact, d_tel, d_address, j_address, j_tel,
                     mailno=None, is_gen_bill_no=None, j_company=None, j_contact=None, j_mobile=None,
                     j_shippercode=None, j_country=None, j_province=None, j_city=None, j_county=None, j_post_code=None,
                     d_mobile=None, d_deliverycode=None, d_country=None, d_province=None, d_city=None, d_county=None,
                     d_post_code=None, custid=None, pay_method=None, express_type=None, parcel_quantity=None,
                     cargo_length=None, cargo_width=None, cargo_height=None, volume=None, cargo_total_weight=None,
                     declared_value=None, declared_value_currency=None, customs_batchs=None, sendstarttime=None,
                     is_docall=None, need_return_tracking_no=None, return_tracking=None, d_tax_no=None, tax_pay_type=None,
                     tax_set_accounts=None, original_number=None, payment_tool=None, payment_number=None, goods_code=None,
                     in_process_waybill_no=None, brand=None, specifications=None, temp_range=None, order_name=None,
                     order_cert_type=None, order_cert_no=None, order_source=None, template=None,
                     remark=None, oneself_pickup_flg=None, dispatch_sys=None, filter_field=None, total_net_weight=None,
                     send_remark_two=None, special_delivery_type_code=None, special_delivery_value=None,
                     realname_num=None, merchant_pay_orde=None, routelabelForReturn=None, routelabelService=None,
                     j_tax_no=None, is_unified_waybill_no=None, send_cert_type=None, send_cert_no=None
                     ):
        """
        下单接口(国内/国际)

        param orderid: 	客户订单号
        param d_company: 到件方公司名称
        param d_contact: 到件方联系人
        param d_tel: 到件方联系电话
        param j_address: 寄件方详细地址 电子面单必填
        param j_tel: 寄件方联系电话 电子运面单必填

        param mailno: 	顺丰运单号,一个订单只能有一个母单号，对于路由推送注册,此字段为必填
        param is_gen_bill_no: 	是否要求返回顺丰运单号: 1:要求 其它为不要求
        param j_company: 寄件方公司名称,如果需要生成电子面单,则为必填。公司件必填
        param j_contact: 寄件方联系人
        param j_mobile: 寄件方手机j_tel和j_mobile必填一个
        param j_shippercode: 寄件方国家/城市代码,跨境件必填
        param j_country: 寄件方国家
        param j_province: 寄件方所在省级行政区名称
        param j_city: 寄件方所在地级行政区名称
        param j_county: 寄件人所在县/区,必须是标准县/区称谓
        param j_post_code: 寄方邮编,跨境件必填
        param d_mobile: 到件方联系电话
        param d_deliverycode: 到件方代码 ，跨境件必填
        param d_country: 到方国家
        param d_province: 到件方所在省份,必须是标准的省名称称谓
        param d_city: 到件方所在城市名称,必须是标准的城市称谓
        param d_county: 到件方所在县/区
        param d_address: 到件方详细地址
        param d_post_code: 到方邮编,跨境件必填
        param custid: 顺丰月结卡号
        param pay_method: 付款方式: 1:寄方付 2:收方付 3:第三方付
        param express_type: 快件产品编码
        param parcel_quantity: 包裹数,一个包裹对应一个运单号,如果是大于1个包裹,则返回则按照子母件的方式返回母运单号和子运单号
        param cargo_length: 客户订单货物总长,单位厘米, 跨境件必填
        param cargo_width: 客户订单货物总宽,单位厘米, 跨境件必填
        param cargo_height: 客户订单货物总高,单位厘米, 跨境件必填
        param volume: 订单货物总体积,单位立方厘米,精确到小数点后3位
        param cargo_total_weight: 订单货物总重量,包含子母件,单位千克,精确到小数点后3位
        param declared_value: 客户订单货物总声明价值, 跨境件必填
        param declared_value_currency: 货物声明价值币别 国内默认CNY 国际默认USD
        param customs_batchs: 报关批次
        param sendstarttime: 上门取件时间要求上门取件开始时间,格式:YYYY-MM-DD HH24:MM:SS
        param is_docall: 是否要求通过手持 终端通知顺丰收派员收件:1:要求 其它为不要求
        param need_return_tracking_no: 是否要求通过手持 终端通知顺丰收派员收件:1:要求 其它为不要求
        param return_tracking: 顺丰签回单服务运单号
        param d_tax_no: 收件人税号（台湾件必传）
        param tax_pay_type: 税金付款方式: 1:寄付 2:到付
        param tax_set_accounts: 税金结算账号
        param original_number: 电商原始订单号
        param payment_tool: 支付工具
        param payment_number: 	支付号码
        param goods_code: 	商品编号
        param in_process_waybill_no: 头程运单号
        param brand: 货物品牌
        param specifications: 货物规格型号
        param temp_range: 温度范围类型,当express_type为12医药温 控件时必填:1为冷藏 3为冷冻
        param order_name: 客户订单下单人姓名
        param order_cert_type: 客户订单下单人证件类型 1、身份证2、护照 3、其他4、统编号5、税号 跨境件必填
        param order_cert_no: 	客户订单下单人证件号 跨境件必填
        param order_source: 客户订单来源(对于平台类客户,如果需要在订单中区分订单来源,则可使用此字段
        param template: 业务模板编码,
        param remark: 备注
        param oneself_pickup_flg: 快件自取;1表示客户同意快件自取; 非1表示客户不同意快件自取
        param dispatch_sys: 订单数据分发的系统编码
        param filter_field: 筛单特殊字段
        param total_net_weight: 商品总净重
        param send_remark_two: 收方邮箱不为空则校验：^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9_-]+)+$
        param special_delivery_type_code: 	特殊派送类型代码1:身份验证
        param special_delivery_value: 特殊派件具体表述
        param realname_num: 实名认证流水号
        param merchant_pay_orde: 商户订单号
        param routelabelForReturn: 签回单路由标签返回 默认0 1:查询 其他:不查询
        param routelabelService: 路由标签查询服务 默认0不查询
        param j_tax_no: 寄件人税号
        param is_unified_waybill_no: 是否使用国家统一面单号 1是 0 不是
        param send_cert_type: 寄件证件类型 
        param send_cert_no: 寄件人证件号码
        """
        pass

    @Service("OrderConfirmService", None, ("OrderConfirmOption", 9))
    def confirm_order(self, orderid, mailno, dealtype="1", customs_batchs=None,
                      agent_no=None, consign_emp_code=None, source_zone_code=None, in_process_waybill_no=None,
                      weight=None, volume=None, return_tracking=None, express_type=None, children_nos=None,
                      waybill_size=None, is_gen_eletric_pic="1"):
        """
        确认/取消订单接口
        mailno: dealtype 为1时必填
        dealtype: 1 确认 2 取消
        """
        pass

    @Service("OrderSearchService")
    def get_order(self, orderid, search_type="1"):
        """
        订单结果查询接口
        参数：
        order_id: 客户订单号
        search_type: 查询类型:1,正向单查询,传入的orderid为正向定单号,2,退货单查询,传入的orderid为退货原始订单号
        """
        pass

    @Service("RouteService", "RouteRequest")
    def get_route_info(self, tracking_number, tracking_type=1, method_type=1, reference_number=None, check_phoneNo=None):
        """
        路由信息查询接口
        param tracking_number: 查询号，根据type不同，含义不同，多个单号以，分割
        param tracking_type: 查询号类别，1 顺丰运单号 2 客户订单号 3 逆向单
        param method_type: 路由查询类别 1:标准路由查询
        param reference_number: 参考编码(目前针对亚马逊客户,由客户传)
        param check_phoneNo: 校验电话号码后四位值;
        return: 包含节点信息的路由，路由信息操作码 见https://qiao.sf-express.com/pages/developDoc/index.html?level2=949000
        """
        pass

    @Service("OrderFilterService", None, ("OrderFilterOption", 4))
    def can_delivery(self, d_address, orderid=None, filter_type=1, j_tel=None, country="CN",
                     province=None, city=None, county=None, d_country="CN", d_province=None,
                     d_city=None, d_county=None, j_address=None, d_tel=None, j_custid=None):
        """
        订单筛选接口
        客户系统通过此接口向顺丰系统发送主动的筛单请求,用于判断客户的收、派地址是否属于顺丰的收派范围。

        param d_address: 到件方详细地址,需要包括省市区
        param orderid: 客户订单号,filter_type=2则必须提供
        param filter_type: 筛单类别:1:自动筛单 2:可人工筛单
        param j_tel: 寄件方电话
        param country: 寄件人所在国家代码
        param province: 寄件方所在省份,必须是标准的省名称称谓 如:广东省,如果是直辖市,请直接传北京、上海等
        param city: 寄件方所属城市名称,必须是标准的城市称谓 如:深圳市。
        param county: 	寄件人所在县/区,必须是标准的县/区称谓,示例:“福田区”。
        param d_country: 到件方国家
        param d_province: 到件方所在省份,必须是标准的省名称称谓 如:广东省,如果是直辖市,请直接传北京、上海等。
        param d_city: 到件方所属城市名称,必须是标准的城市称谓 
        param d_county: 到件方所在县/区,必须是标准的县/区称谓
        param j_address: 寄件方详细地址,包括省市区,
        param d_tel: 到件方电话
        param j_custid: 结账号,用于在人工筛单时,筛单人员识别客户使用
        """
        pass
