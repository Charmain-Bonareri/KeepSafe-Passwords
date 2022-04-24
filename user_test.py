from user import User
import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        """
            Set up method to run before each test cases.
        """       
        self.new_user = User("CharmainB","charmb@gmail.com","Mogz123!") # create user object


    