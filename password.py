class User:
    """
    Holds all the user data
    """
    user_list=[]
    def __init__(self,firstname,lastname,password):
        """
        Args:
        firstname:New User firstname
        lastname: New User lastname
        password:New User password
        """
        self.firstname= firstname
        self.lastname = lastname
        self.password= password
