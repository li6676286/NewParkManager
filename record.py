'''停车记录的类'''

import random

class ParkingRecord():
    def __init__(self,record_id,into_park_time,into_port_time,
                leave_park_time,leave_port_time,car_number):
        self.record_id=record_id
        self.into_park_time=into_park_time
        self.into_port_time=into_port_time
        self.leave_park_time=leave_park_time
        self.leave_port_time=leave_port_time
        self.car_number=car_number

    def produce_record(self,name,number,into_time,into_port_time,leave_port_time,leave_time):
        print('此次场景停车记录:')
        print('          记录编号:00000001')
        print('          车主:'+name)
        print('          车牌:'+number)
        print('          进入停车场时间:'+into_time)
        print('          进入车位时间:'+into_port_time)
        print('          离开车位时间:'+leave_port_time)
        print('          离开停车场时间:'+leave_time)


