import unittest
from PartA import Vehicle, ChildVehicle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        # Creating instance object for testing
        self.vehicle = Vehicle("Honda", 2010, 180, 120000, "Blue")
        self.child_vehicle = ChildVehicle("Tesla", 2022, 200, 30000, "White", ["Alice", "Bob"])

    # B2 Unit tests to test if an object is an instance of a class.
    def test_instance(self):
        self.assertIsInstance(self.vehicle, Vehicle)
        self.assertIsInstance(self.child_vehicle, ChildVehicle)

    # B3 unit tests to test if an object is NOT an instance of a class.
    def test_not_instance(self):
        self.assertNotIsInstance(self.vehicle, ChildVehicle)
        self.assertNotIsInstance(self.child_vehicle, Vehicle)  # As ChildVehicle extends Vehicle, test accordingly

    # B4: Test if two objects are identical
    def test_identical_objects(self):
        another_vehicle = self.vehicle  
        self.assertIs(self.vehicle, another_vehicle)

    def test_objects_are_not_identical(self):
        another_vehicle = Vehicle("Toyota", 2015, 190, 140000, "Black")
        self.assertIsNot(self.vehicle, another_vehicle)  

    # B5 B5. For task A4 write a set of unit tests to test if update methods work correctly.
    def test_update_methods(self):
        # Test update_name
        self.vehicle.update_name("Toyota")
        self.assertEqual(self.vehicle.name, "Toyota")

        # Test update_year
        self.vehicle.update_year(2015)
        self.assertEqual(self.vehicle.year, 2015)

        # Test update_max_speed
        self.vehicle.update_max_speed(190)
        self.assertEqual(self.vehicle.max_speed, 190)

        # Test update_mileage
        self.vehicle.update_mileage(140000)
        self.assertEqual(self.vehicle.mileage, 140000)

        # Test update_colour
        self.vehicle.update_colour("Black")
        self.assertEqual(self.vehicle.colour, "Black")

    #Unit tests for ChildVehicle update methods
    def test_update_owners(self):
        self.child_vehicle.update_owners(["Alice", "Charlie"])
        self.assertEqual(self.child_vehicle.owners, ["Alice", "Charlie"])

# B6: Write a main function to run the tests of tasks B2 to B5.
if __name__ == "__main__":
    unittest.main()
