# Drone Mission with inheritance class cameradrone

class Drone:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        self.arm = False
        self.altitude = 0

    def arming(self):
        self.arm = True
        print(f"{self.name} is Arming")

    def disarm(self):
        self.arm = False
        print(f"{self.name} is disarming")


    def takeoff(self, height):
        
        if height  > 0 and self.arm == True :
            self.altitude = height 
            print(f"{self.name} Drone is taking off to height {self.altitude} m")
        else:
            print(f"invalid height input OR {self.name} is not armed")
            self.altitude = 0
            return

    def land(self):
        self.altitude = 0
        print(f"{self.name} Drone is landing")
        self.arm = False

    def consume_battery(self, amount):
        if amount < 0:
            print("invalid input")
            return

        else: 
            self.battery -= amount

    def status(self):
        print(f"Name : {self.name}\n"
              f"Battery : {self.battery} % \n"
              f"Armed : {self.arm}\n "
              f"Height : {self.altitude}\n ")
        
class CameraDrone(Drone):
    def take_picture(self):
        print("taking picture")

    def record_video(self):
        print("Video start recording")

    def takeoff(self, height):
        super().takeoff(height)
        print("Camera Initialized")
    

drone1 = CameraDrone("Ascend", 100)
drone1.takeoff(2)
drone1.status()
drone1.take_picture()

drone1.arming()
drone1.takeoff(10)
drone1.consume_battery(20)
drone1.record_video()
drone1.status()
drone1.land()

drone1.status()