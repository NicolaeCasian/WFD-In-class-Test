import unittest
from PartA import Vehicle, ChildVehicle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        # Creating instance object for testing
        self.vehicle = Vehicle("Lexus", 2010, 180, 120000, "Blue")
        self.child_vehicle = ChildVehicle("BMW", 2022, 200, 30000, "White", ["Stanley", "Aaron"])

    # B2 Unit tests to test if an object is an instance of a class.
    def test_instance(self):
        self.assertIsInstance(self.vehicle, Vehicle)
        self.assertIsInstance(self.child_vehicle, ChildVehicle)

    # B3 unit tests to test if an object is NOT an instance of a class.
    # B3: Test if an object is NOT an instance of a class
    def test_not_instance_of_unrelated_class(self):
        testcar = "This is not a vehicle object"
        self.assertNotIsInstance(testcar, Vehicle)  


    # B4: Test if 2 objects are identical
    def test_identical_objects(self):
        another_vehicle = self.vehicle  
        self.assertIs(self.vehicle, another_vehicle)
    #Test if 2 object are not identical
    def test_not_identical_objects(self):
        another_vehicle = Vehicle("VW", 2015, 170, 190000, "Black")
        self.assertIsNot(self.vehicle, another_vehicle)  

    #B5. For task A4 write a set of unit tests to test if update methods work correctly.
    def test_update_methods(self):
        # Test update_name method
        self.vehicle.update_name("Toyota")
        self.assertEqual(self.vehicle.name, "Toyota")

        # Test update_year method
        self.vehicle.update_year(2025)
        self.assertEqual(self.vehicle.year, 2025)

        # Test update_max_speed method
        self.vehicle.update_max_speed(240)
        self.assertEqual(self.vehicle.max_speed, 240)

        # Test update_mileage method
        self.vehicle.update_mileage(240000)
        self.assertEqual(self.vehicle.mileage, 240000)

        # Test update_colour method
        self.vehicle.update_colour("Yellow")
        self.assertEqual(self.vehicle.colour, "Yellow")

    #Unit tests for ChildVehicle update methods
    def test_update_owners(self):
        self.child_vehicle.update_owners(["Nico", "Girish"])
        self.assertEqual(self.child_vehicle.owners, ["Nico", "Girish"])

# B6: Write a main function to run the tests of tasks B2 to B5.
if __name__ == "__main__":
    unittest.main()
