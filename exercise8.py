# drone fleet

class Drone:
    def __init__(self, name):
        self.armed = False
        self.name = name


    def arm(self):
        if self.armed:
            print("The drone fleet is not armed")
            return
        else:
            self.armed = True
            print("All Fleet are arming")        

    def takeoff(self,height):
        if self.armed == True:
            if height < 0:
                print("invalid input")

            else:
                self.height = height
                print(f"The fleet is taking off to height {self.height}")

        else:
            print("The Drone Fleet is not Armed")
            

    def land(self):
        self.height = 0
        print("All Drone are set to land mode")
        self.armed = False


    def status(self):
        pass


if __name__ == "__main__":
    
    fleet = []
    num = int(input("Enter the total numbers of Drone in a fleet\n"))
    if num < 0:
        print("invalid number")
    else:
        for i in range(num):
            drone = Drone("d{i}")
            fleet.append(drone)

    arm =input("want to arm drone fleet?  yes/no\n").lower()
    if arm == "yes":
        for drone in fleet:
           drone.arm()
           

    else:
        ("fleet stay in disarm")

    fly = input("want to fly?   yes/no\n").lower()
    if fly == "yes":
        for drone in fleet:
            drone.takeoff(2)

    else:
        pass

    land =input ("want to land?  yes/no\n").lower()
    if land == "yes":
        Drone.land()

    else:
        pass
            
        

    


    


