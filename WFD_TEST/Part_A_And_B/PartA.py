# A2 Creating a class with the Vehcile attributes
class Vehicle:
    def __init__(self, name, year, max_speed, mileage, colour):
        self.name = name
        self.year = year
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour

    # A3: Creating a function which prints all the init attributes
    def print_attributes(self):
        print(f"Vehicle name: {self.name}, Year: {self.year}, Max Speed: {self.max_speed}, "
              f"Mileage: {self.mileage}, Colour: {self.colour}")

    # A4 Updating the init attributes
    #This function updates the name 
    def update_name(self, name):
        if isinstance(name, str):
            self.name = name

    #This function updates the year
    def update_year(self, year):
        if isinstance(year, int):
            self.year = year
    #This function updates the max speed
    def update_max_speed(self, max_speed):
        if isinstance(max_speed, (int, float)):
            self.max_speed = max_speed
    #This function updates the milage
    def update_mileage(self, mileage):
        if isinstance(mileage, (int, float)):
            self.mileage = mileage
    #This function updates the colour
    def update_colour(self, colour):
        if isinstance(colour, str):
            self.colour = colour

# A5 Creating a child class linked to the main class Vehicle
class ChildVehicle(Vehicle):
    def __init__(self, name, year, max_speed, mileage, colour, owners):
        super().__init__(name, year, max_speed, mileage, colour)
        self.owners = owners

    # A6 Printing the attributes and adding the new attribute Owners
    def print_attributes(self):
        super().print_attributes()
        print(f"Owners: {self.owners}")

    # A7 Updating the new attribute Owners
    def update_owners(self, owners):
        if isinstance(owners, (list, str)):  
            self.owners = owners

# Task A8: Creating instances to test
vehicle = Vehicle("BMW", 2010, 180, 120900, "Blue")
child_vehicle = ChildVehicle("Mercedes", 2022, 200, 10000, "White", ["Nico", "Girish"])

# Task A9: Call the methods to print attributes
print("A9: Vehicle from main class")
vehicle.print_attributes()
print("\nVehicle from Child class")
child_vehicle.print_attributes()

# Task A10: Perform examples of updates
print("\na10 Updating Attributes")

# Update methods for attributes in the vehicle class
vehicle.update_name("Toyota")
vehicle.update_year(2015)
vehicle.update_max_speed(190)
vehicle.update_mileage(140000)
vehicle.update_colour("Black")

# Update methods for attributes in the child class
child_vehicle.update_owners(["Stanley", "Akosh"])

# Print updated attributes
print("\nUpdated Attributes of the Vehicle class: ")
vehicle.print_attributes()
print("\nUpdated Attributes of ChildVehicle class: ")
child_vehicle.print_attributes()
