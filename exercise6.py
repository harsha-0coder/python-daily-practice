# Hospital management 

class Patient:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    def admit(self, disease):
        self.disease = disease
        print(f"{self.name} is admit for {self.disease}")
        

    def discharge(self):
        print(f"{self.name} has good condition and ready to discharge")

    def status(self):
        print(f"name : {self.name}\n"
              f"age : {self.age}\n"
              f"disease : {self.disease}\n")
        
pat1 =Patient("Harsh", 25)
pat1.admit("cancer")
pat1.status()
pat1.discharge()