# task 1 
#construct the class , define attributes, and create methods
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner

    def print_vehicle(self):
        print(f"Vehicle type: {self.vehicle_type}\nRegistration Number: {self.reg_num}\nOwner: {self.owner}")
    
    def update_owner(self, new_owner):
        self.owner = new_owner

#define vehicle  calling on vehicle class 
vehicle_one  = Vehicle("123456", "Honda Civic", "John")
vehicle_two  = Vehicle("123456", "Rolls Royce", "Steve")
vehicle_three  = Vehicle("123456", "Toyota Corolla", "Jordan")

#update the owners using the update_owner method 
vehicle_one.update_owner("Jim")
vehicle_two.update_owner("Bob")
vehicle_three.update_owner("Terry")

#print the vehicles using the print vehicle method 
vehicle_one.print_vehicle()
print("\n")
vehicle_two.print_vehicle()
print("\n")
vehicle_three.print_vehicle()

#define class event, with attributes and methods to add and print number participants 
class Event: 
    def __init__(self, name, date):
        self.name = name 
        self.date = date
        self.participants = [] 

    def add_participant(self):
        while True: 
            part_name = input("\nAdd name: ")
            part_date = input("\nAdd date: ")
            self.participants.append((part_name, part_date))
            try_again = input("Would you like to add another participant?(Y,N): ")
            while try_again not in ["Y", "N"]:
                try_again = input("Please type Y or N: ")
            if try_again == "N": 
                break 

    def get_participant_count(self):
        num_part = len (self.participants)
        print(f"\nNumber of paticipants: {num_part}")

#show how the code works 
event = Event("Meeting", "Date")
event.add_participant()
event.get_participant_count()




    



    
    



