from user import User
import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        """
            Set up method to run before each test cases.
        """       
        self.new_user = User("CharmainB","charmb@gmail.com","Mogz123!") # create user object


    def test_init(self):
        """
            Test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "CharmainB")        
        self.assertEqual(self.new_user.email, "charmb@gmail.com")
        self.assertEqual(self.new_user.password, "Mogz123!")


if __name__ == '__main__':
    unittest.main()