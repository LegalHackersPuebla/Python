class Car():
    def __init__(self,brand,model,km,num_passengers):
        self.brand=brand
        self.model=model
        self.km=km
        self.num_passengers=num_passengers
    
    def get_brand(self):
        print('The brand is: '+ self.brand)

class Battery():
    def __init__(self,brand='LTH',battery_capacity=70,serial_number=12345):
        self.brand=brand
        self.battery_capacity=battery_capacity
        self.serial_number=serial_number
        
        
class Electricar(Car):
    def __init__(self,brand,model,km,num_passengers):
        super().__init__(brand,model,km,num_passengers)
        self.battery=Battery()
        





