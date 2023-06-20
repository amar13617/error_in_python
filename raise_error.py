class Garage:
    
    def __init__(self):
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def add_car(self,car):
        #print("this method work in progress")
        raise NotImplementedError("we cannot add car to the garage")
        
ford = Garage()
print(ford.add_car("bmw"))
print(len(ford))




