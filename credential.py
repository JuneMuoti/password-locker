class Credentials:
    """
    Holds all credential data
    """
    credential_list = []
    def __init__(self,account_name,account_password):
        """
        defines the diffrent instances of the credential class
        """
        self.account_name = account_name
        self.account_password = account_password
