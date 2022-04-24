
class User:
    """
   Class that generates new instances of users.
    """

    user_list=[]; # Empty user list

    def __init__(self, username, email, password):
        self.username=username
        self.email=email
        self.password=password
        

