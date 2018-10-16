'''一个车的类'''
class Car():

    def __init__(self,car_number,car_color,contact_model,car_brand):
        self.car_number=car_number         #车牌号
        self.car_color=car_color           #颜色
        self.contact_model=contact_model   #车型号
        self.car_brand =car_brand          #车品牌

#     def __str__(self):
#         return "%s %s %s %s" %(self.car_number,self.car_color,self.contact_model,self.car_brand)
