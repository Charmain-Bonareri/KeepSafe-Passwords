

class User:
    """
   Class that generates new instances of users.
    """

    user_list=[]; # Empty user list

    def __init__(self, username, email, password):
        self.username=username
        self.email=email
        self.password=password

    
    def save_user(self):
        """
        Save_user method saves user objects into user_list
        """
        User.user_list.append(self)
        
class Credential:
    """
    Class that generates new credentials for users.
    """

    credential_list = []; #Empty credentials list

    def __init__(self, username, email,phone_number, password):
        self.username = username
        self.email = email   
        self.phone_number = phone_number         
        self.password = password

    def save_userInfo(self):
        """
        Save_user method saves user objects into user_list
        """
        Credential.credential_list.append(self)

    def delete_passwords(self):
        """
        delete_password method deletes a saved password from the credential_list
        """
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns password details that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Password details of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.phone_number == number:
                return credential

    @classmethod
    def passwords_exist(cls, number):
        """
        A method that checks if a password exists from the credential list.
        Args:
            number: Phone number to search if it exists
        Returns :
            True or false depending if the contact exists
        """
        for credential in cls.credential_list:
            if credential.phone_number == number :
                return True
        return False
   
