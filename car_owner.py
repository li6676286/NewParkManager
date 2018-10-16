'''车主的类'''
class CarOwner():

    def __init__(self,car_owner_id,owner_name,contact_way,owner_car):
        self.car_owner_id=car_owner_id  #车主编号
        self.owner_name=owner_name      #车主名称
        self.contact_way=contact_way    #车主联系方式
        self.owner_car =owner_car       #车主的车

    def into_park(self,owner_name,owner_car_number,park_name):
        print(owner_name+'驾驶车牌号为'+owner_car_number+'的车进入'+park_name)

    def into_port(self,owner_name,owner_car_number,park_name,port_id):
        print(owner_name+'将车牌号为'+owner_car_number+'的车停入了'+park_name+port_id+'号车位')

    def happy(self,owner_name):
        print(owner_name+'出去happy了一段时间')

    def leave_port(self,owner_name,port_id):
        print(owner_name+'开车离开了'+port_id+'号车位')

    def leave_park(self,owner_name,owner_car_number,park_name):
        print(owner_name+'将车牌号为'+owner_car_number+'的车开到'+park_name+'的出口,准备离开')

    def pay(self,owner_name):
        print(owner_name+'缴纳了车费并离开了停车场')
