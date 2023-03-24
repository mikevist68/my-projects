#inheritance

# Pyhton conventions:
# 1. Class names should normally use the CapWords convention.
# 2. Function names should be lowercase, with words seperated by underscores as necessary to improve readability.
# 3. Always use self for the first argument to instance methods.
# 4. Multiline comments should use the # for each line. Don't use docstring - i cheated before!

# creating an object from a class, nerds call it creating an instance.


class AutoMobile:
    '''-> Automobile base / parent class'''

    model_year = "2019"

    def start(self):
        print("Automobile is starting ... vroom, vroom!")

    def turn_off(self):
        '''-> shut off auto ... '''
        print("Click, pud, pud ... thud. vechile is off.")


class Truck(AutoMobile):
    '''-> Truck - a type of automobile. '''

    def __init__(self, year=None):
        if year is None:
            self.year = 2018
        else:
            self.year = year

    def __str__(self):
        return "2019 vechile sold by Studioweb."

    def dumpload(self, value=None):
        if value is None:
            print("Truck has nothing to dump.")
        else:
            print("Truck is dumping " + (str(value)))

    def truck_year(self):
        print("This truck was built in:" + str(self.year))

    #overiding method
    #def start(self):
        print("Truck is starting ... puda, puda, vroom!")

    #def turn_off(self):
        #'''-> shut off truck ...'''
        #print("Click, puda, puda ... thud. Truck is off.")


my_truck = Truck("2021")
my_truck.truck_year()

my_truck.dumpload()
my_truck.dumpload("2000lbs")

#print(my_truck)

#my_truck.start()
#my_truck.turn_off()

#create a new truck, but dont specify the year
another_truck = Truck()
another_truck.truck_year()

print(type(another_truck))
