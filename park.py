'''停车场的类'''
class Park():
    
    def __init__(self,park_name,max_car,park_address,free_port):
        self.park_name=park_name
        self.max_car=max_car
        self.park_address=park_address
        self.free_port=free_port

    def produce_record(self):
        print('停车场产生了停车记录')

    def update_record(self):
        print('停车场修改了停车记录')

    def produce_order(self,park_time,pay_way,leave_time,name,pay_status):
        consumption = ((park_time) / 3600) * 5
        print('停车场根据此次停车记录计算费用并生成订单')
        print('          订单编号:000001')
        print('          应付金额:'+str(consumption)+'元')
        print('          支付方式:'+pay_way)
        print('          支付时间:'+leave_time)
        print('          支付人:'+name)
        print('          支付状态:'+pay_status)




