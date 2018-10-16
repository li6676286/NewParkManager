'''订单类'''
class Oeder():
    
    def __init__(self,order_id,pay_money,pay_way,pay_time,pay_man,
                pay_status):
        self.order_id=order_id         #订单编号
        self.pay_money=pay_money       #订单金额
        self.pay_way=pay_way           #支付方式
        self.pay_time=pay_time         #支付时间
        self.pay_man=pay_man           #支付人
        self.pay_status=pay_status     #支付状态