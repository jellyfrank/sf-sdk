#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm, Service
import inspect


class Order(Comm):

    @Service("OrderService")
    def create_order(self, orderid, d_company, d_contact, d_tel, d_address, j_address, j_tel,
                     d_mobile=None, d_province=None, d_city=None, d_county=None, mailno=None, custid=None,
                     j_province=None, j_city=None, j_county=None,
                     j_company=None, j_contact=None,  j_mobile=None, pay_method=None, express_type=None, parcel_quantity=None,
                     cargo_length=None, cargo_width=None, cargo_height=None, volume=None, cargo_total_weight=None, sendstarttime=None,
                     is_docall=None, need_return_tracking_no=None, return_tracking=None, temp_range=None, template=None,
                     remark=None, oneself_pickup_flg=None, special_delivery_type_code=None, special_delivery_value=None,
                     realname_num=None, routelabelForReturn=None, routelabelService=None, is_unified_waybill_no=1
                     ):
        """
        下单接口
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
        search_type: 查询类型:1,正向单查询,传入
的orderid为正向定单号,2,退货单查询,传入的orderid
为退货原始订单号
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
