class vehicle:
    curr_speed=0
    
    def __init__(self,name,model):
        self.name=name
        self.model=model
        
    def start(self,start_speed):
        self.curr_speed=start_speed
        print("vehicle has started")
        
    def acc(self,acc_speed):
        self.curr_speed=self.curr_speed+acc_speed
        if self.curr_speed>=120:
            print("vehicle speed "+ self.curr_speed+ "has exceeded speed limit. Apply brake")
        
    def brake(self,brake_speed):
        self.curr_speed=self.curr_speed-brake_speed
        if self.curr_speed<=0:
            print("vehicle has reached minimum speed")
        
    def stop(self):
        self.curr_speed = 0
        print("vehicle has stopped")
        
    def print_Status(self):
        print("vehicle name is "+self.name)
        print("vehicle model is "+str(self.model))
        print("vehicle's current speed is "+str(self.curr_speed))
        print("------------------------------------------")
        
v1=vehicle("verna",2016)
v1.start(20)
v1.acc(20)
v1.acc(100)
#v1.stop()
v1.print_Status()

v2=vehicle("verna",2016)
v2.start(30)
v2.acc(15)
#v2.stop()
v2.print_Status()