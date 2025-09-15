#if t6he name of the class is car then the data attribute can be the name, manufacturer, color, year, and cc and manymore.
# th4e method amy be start,break,drtive, tur4n,a dn dchange the gaier and  maympore

#making class

#class ClassName:
    #<statement-1>
    #<statement-N>


class Car:
    name="premio"
    color="white"

    def start():
        print("starting the engine")


print("Name of the car is:",Car.name)
print("the color of the car is:",Car.color)


Car.start()

# a question may apper here that all the car names wont be the premio and the wont be the white . what can we do?
# the answer is the ," assingn empty sting within the class. then try to chane during calliung the them.

class Car:
    name=""
    color=""


    def start(self):
        print("Starting the car")




#lets make an object within the class car

my_car=Car()
my_car.name="Axio"
print(my_car.name)
my_car.start()


class Car:
    name=""
    color=""


    def __init__(self, name,color):
        self.name=name
        self.color=color


    def start(self):
        print("starting the engine")


my_car=Car("Corolla", "white")
print(my_car.name)
print(my_car.color)

my_car.start()

#above three name ate different including "name="",self.name and name inside the __init__ method

class Car:
    def __init__(self,n,c):
        self.name = n
        self.color=c

    def start(self):
        print("Starting the car")

my_car=Car("Corolla","white")

print(my_car.name)
print(my_car.color)
my_car.start()


#if the methofds of the class whould like to access the object's attribute then


class Car:
    def __init__(self,n,c):
        self.name = n
        self.color=c

    def start(self):
        print("name",self.name)
        print("coloc",self.color)
        print("starting the car")

my_car=Car("Corolla","white")


Car.start(my_car)


#Now we will makt the more than one objects

class Car:
    def __init__(self,n,c):
        self.name = n
        self.color=c

    def start(self):
        print("name",self.name)
        print("coloc",self.color)
        print("starting the car")

my_car=Car("Corolla","white")

my_car.start()

my_car1=Car("premio","ack")
my_car1.start()
