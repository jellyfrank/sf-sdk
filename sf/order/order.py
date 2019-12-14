#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm
import inspect


class Order(Comm):

    def create_order(self, orderid, d_company, d_contact, d_tel, d_address, j_address, j_tel,
                     d_mobile=None, d_province=None, d_city=None, d_county=None, mailno=None, custid=None,
                     j_province=None, j_city=None, j_county=None,
                     j_company=None, j_contact=None,  j_mobile=None, pay_method=None, express_type=None, parcel_quantity=None,
                     cargo_length=None, cargo_width=None, cargo_height=None, volume=None, cargo_total_weight=None, sendstarttime=None,
                     is_docall=None, need_return_tracking_no=None, return_tracking=None, temp_range=None, template=None,
                     remark=None, oneself_pickup_flg=None, special_delivery_type_code=None, special_delivery_value=None,
                     realname_num=None, routelabelForReturn=None, routelabelService=None, is_unified_waybill_no=None
                     ):
        """
        下单接口
        """
        data = {
            "service": "OrderService",
            "data": {
                "Order": {
                    "is_unified_waybill_no": "1"
                }
            }
        }

        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        for i in args:
            if values[i] and i != 'self':
                data["data"]["Order"][i] = values[i]

        return self.post(data)

    def confirm_order(self, orderid, mailno, dealtype="1", customs_batchs=None, agent_no=None, consign_emp_code=None, source_zone_code=None, in_process_waybill_no=None,
                      weight=None, volume=None, return_tracking=None, express_type=None, children_nos=None, waybill_size=None, is_gen_eletric_pic="1"):
        """确认/取消订单接口"""
        data = {
            "service": "OrderConfirmService",
            "data": {
                "OrderConfirm": {
                    "OrderConfirmOption": {

                    }
                }
            }
        }

        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        for i in args:
            if i != "self":
                if i in ("weight", "volume", "return_tracking", "express_type", "children_nos", "waybill_size", "is_gen_eletric_pic"):
                    data["data"]["OrderConfirm"]["OrderConfirmOption"][i] = values[i]
                elif values[i]:
                    data["data"]["OrderConfirm"][i] = values[i]

        return self.post(data)

    def get_order(self, orderid, search_type="1"):
        """
        订单结果查询接口
        参数：
        order_id: 客户订单号
        search_type: 查询类型:1,正向单查询,传入
的orderid为正向定单号,2,退货单查询,传入的orderid
为退货原始订单号
        """

        data = {
            "service": "OrderSearchService",
            "data": {
                "OrderSearch": {
                    "orderid": orderid,
                    "search_type": search_type
                },
            }
        }

        return self.post(data)

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

        data = {
            "service": "RouteService",
            "data": {
                "RouteRequest": {
                    "tracking_number": tracking_number
                }
            }
        }

        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        for i in args:
            if values[i] and i != 'self':
                data["data"]["RouteRequest"][i] = str(values[i])

        return self.post(data)
