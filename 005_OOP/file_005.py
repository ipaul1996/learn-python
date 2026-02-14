# If the same attribute name occurs in both an instance and in a class, then attribute 
# lookup prioritizes the instance:

class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region) # storage west

w2 = Warehouse()
w2.region = 'east' # instance variable which will shadow the class variable region
print(w2.purpose, w2.region) # storage east

