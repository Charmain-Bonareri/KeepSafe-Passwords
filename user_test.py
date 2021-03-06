from user import User, Credential
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

    def test_save_user(self):
        """
            Test_save_user test case to test if the user object is saved into
            the user list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class CredentialTest(unittest.TestCase):
    def setUp(self):
        """
            Set up method to run before each test cases.
        """       
        self.new_credential = Credential("Snapchat", "CharmainB","charmb@gmail.com","0712345678", "Mogz123!") # create userinfo object


    def test_init(self):
        """
            Test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.KeepSafeAccount, "Snapchat")  
        self.assertEqual(self.new_credential.username, "CharmainB")        
        self.assertEqual(self.new_credential.email, "charmb@gmail.com")   
        self.assertEqual(self.new_credential.phone_number, "0712345678")    
        self.assertEqual(self.new_credential.password, "Mogz123!")

    def test_save_user(self):
        """
            Test_save_user test case to test if the user object is saved into
            the user list
        """
        self.new_credential.save_userInfo()
        self.assertEqual(len(Credential.credential_list),1)
    
    def test_save_many_passwords(self):
        '''
            Test_save_multiple_passwords to check if we can save multiple passwords
            objects to our credential_list
        '''
        self.new_credential.save_userInfo()
        test_credential = Credential("Snapchat", "CharmainB","charmb@gmail.com","0712345678", "Mogz123!") 
        test_credential.save_userInfo()
        self.assertEqual(len(Credential.credential_list),2)

    def tearDown(self):
        '''
            TearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_delete_passwords(self):
        """
            Test_delete_passwords to test if we can remove a password from our credential list
        """
        self.new_credential.save_userInfo()
        test_credential = Credential("Snapchat", "CharmainB","charmb@gmail.com","0712345678", "Mogz123!")
        test_credential.save_userInfo()

        self.new_credential.delete_passwords()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_passwords(self):
        """
            Test to check if we can find credential details by phone number and display information
        """
        self.new_credential.save_userInfo()
        test_credential = Credential("Snapchat", "CharmainB","charmb@gmail.com","0712345678", "Mogz123!") 
        test_credential.save_userInfo()

        found_password = Credential.find_by_number("0712345678")

        self.assertEqual(found_password.email,test_credential.email)

    def test_passwords_exist(self):
        """
            Test to check if we can return a true if we can find the contact
            and false if we cannot find the contact.
        """
        self.new_credential.save_userInfo()
        test_password = Credential("Snapchat", "CharmainB","charmb@gmail.com","0712345678", "Mogz123!")
        test_password.save_userInfo()
        found_password = Credential.passwords_exist("0712345678")
        self.assertTrue(found_password)

    def test_display_all_passwords(self):
        '''
            A method that returns all password details that has been saved by the user
        '''

        self.assertEqual(Credential.display_passwords(),Credential.credential_list)

    


if __name__ == '__main__':
    unittest.main()