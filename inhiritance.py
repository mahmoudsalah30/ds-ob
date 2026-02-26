class vechile :
    def __init__(self,a,b=None):
        self.seats=a
        if b==None :
            self.passeengers=[]
        else :
            self.passeengers=b
    def print_passengers(self):
        for i in range(len(self.passeengers)):
            print(self.passeengers[i])
    def add (self,name):
        self.passeengers.append(name)
class motorcycle(vechile):
    def __init__(self,b,c):
        self.seats=2
        self.passeengers=b
        self.brand=c
    def add(self,name):
        if len(self.passeengers) < self.seats :
            self.passeengers.append(name)
        else:
            print('The vehicle is full')
        
moto1=motorcycle(['mohamed','omar'],'byd')
moto1.add('salah')       
moto1.print_passengers()



class convoy():
    def __init__(self):
          self.vehicle_list=[]
          self.length=1
          self.vehicle_list.append(vechile(4))
    def add_vechile(self,vechile1):
        self.vehicle_list.append(vechile1)
        self.length=self.length+1
convoy1 =convoy()
convoy1.vehicle_list[0].add('albert')

convoy1.add_vechile(motorcycle('Raphael','Honda'))



for i in (convoy1.vehicle_list):
    i.print_passengers()