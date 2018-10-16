from car import Car
from car_owner import CarOwner
from port import Port
from park import Park
from record import ParkingRecord
import random
import time
'''给定各项数据'''

car1 = Car('辽A12345','红色','A6','奥迪')
car2 = Car('辽B12345','黄色','745','宝马')
car3 = Car('辽C12345','蓝色','GLC','奔驰')
car4 = Car('辽D12345','黑色','DSG','迈腾')
car5 = Car('辽E12345','白色','CS35','长安')

car_list = [car1,car2,car3,car4,car5]

owner1 = CarOwner('1','Uzi','13845789865',car1)
owner2 = CarOwner('2','Letme','14578956858',car2)
owner3 = CarOwner('3','Xiaohu','15858585858',car3)
owner4 = CarOwner('4','Mlxg','16688666688',car4)
owner5 = CarOwner('5','Ming','17985465258',car5)

owner_list = [owner1,owner2,owner3,owner4,owner5]

port1 = Port('5',5,'0')
port2 = Port('15',5,'0')
port3 = Port('25',5,'0')

port_list = [port1,port2,port3]

park1 = Park('浑南停车场',100,'浑南',100)
park2 = Park('大东停车场',100,'大东',100)
park3 = Park('沈河停车场',100,'沈河',100)

park_list = [park1,park2,park3]

'''随机一次场景的各项属性'''
this_owner = random.sample(owner_list,1)  #随机一个车主
this_park = random.sample(park_list,1)    #随机一个停车场
this_port = random.sample(port_list,1)    #随机一个车位

name = this_owner[0].__dict__.get('owner_name')  #车主姓名
number = this_owner[0].__dict__.get('owner_car').__dict__.get('car_number') #车牌号
park = this_park[0].__dict__.get('park_name') #停车场名称
port = this_port[0].__dict__.get('port_id') #车位编号

way_time = float(random.sample(range(60,181),1)[0]) #随机生成从出入口到车位的时间
stay_time = float(random.sample(range(3600,7201),1)[0]) #随机生成车在停车场停留的时间

into_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) #取系统时间做进入停车场的时间
into_port_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(way_time+time.time())) #进入车位的时间
leave_port_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(way_time+time.time()+stay_time)) #离开车位时间
leave_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(way_time*2+time.time()+stay_time)) #离开停车场的时间

print('停车模拟场景开始:')

owner1.into_park(name,number,park)
park1.produce_record()
owner1.into_port(name,number,park,port)
park1.update_record()
owner1.happy(name)
owner1.leave_port(name,port)
park1.update_record()
owner1.leave_park(name,number,park)

record = ParkingRecord('00000001',into_time,into_port_time,leave_time,leave_port_time,number)
record.produce_record(name,number,into_time,into_port_time,leave_port_time,leave_time)

park1.produce_order(stay_time,'支付宝',leave_time,name,'未支付')

owner1.pay(name)

print('停车模拟场景结束')