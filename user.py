class User:
    """
    Holds all the user data
    """
    user_list=[]
    def __init__(self,first_name,last_name,password):
        """
        Args:
        firstname:New User firstname
        lastname: New User lastname
        password:New User password
        """
        self.first_name= first_name
        self.last_name = last_name
        self.password= password
