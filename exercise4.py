# Drone Mission

class Drone:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        self.arm = False

    def arming(self):
        self.arm = True
        print(f"{self.name} is Arming")

    def disarm(self):
        self.arm = False
        print(f"{self.name} is disarming")


    def takeoff(self, height):
        self.altitude = height
        if height  > 0 and self.arm == True :
            self.altitude = height 
            print(f"{self.name} Drone is taking off to height {self.altitude} m")
        else:
            print(f"invalid height input OR {self.name} is not armed")
            self.altitude = 0

    def land(self):
        self.altitude = 0
        print(f"{self.name} Drone is landing")
        self.arm = False

    def consume_battery(self, amount):
        self.battery -= amount
        if self.battery < 0:
            print("invalid input")
            self.battery = 0

        else: 
            self.battery 

    def status(self):
        print(f"Name : {self.name}\n"
              f"Battery : {self.battery} % \n"
              f"Armed : {self.arm}\n "
              f"Height : {self.altitude}\n ")
      

drone1 = Drone("Ascend", 100)
drone1.takeoff(2)
drone1.status()

drone1.arming()
drone1.takeoff(10)
drone1.consume_battery(20)
drone1.status()
drone1.land()

# drone1.status()