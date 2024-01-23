class mobile:

    def __init__(self,Battery,RAM,Memory):
        self.battery=Battery
        self.ram=RAM
        self.memory=Memory

    def specify(self):
        print("Battery range : ",self.battery)
        print("With ",self.ram," RAM")
        print("Internal memory : ",self.memory)

SAMSUNG=mobile("5000Mah","8GB","128GB")
print("~~~~~~~~~~~SAMSUNG MOBILE~~~~~~~~~~~")
SAMSUNG.specify()

REDMI=mobile("5000Mah","6GB","64GB")
print("~~~~~~~~~~~REDMI MOBILE~~~~~~~~~~~")
REDMI.specify()

VIVO=mobile("5000Mah","4GB","32GB")
print("~~~~~~~~~~~VIVO MOBILE~~~~~~~~~~~")
VIVO.specify()
