
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

   
