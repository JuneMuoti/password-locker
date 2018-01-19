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
    def save_credential(self):
        """
        save_credential method saves credentials into the credials list
        """
        Credentials.credential_list.append(self)
    def delete_credential(self):
        """
        this is a method to delete a credential from the list of Credentials
        """
        Credentials.credential_list.remove(self)
    def find_by_account_name(cls,account_name):
        """
        takes in an account name and returns a password that matched that account name
        """
        Args:
            account_name: account ame to search for
        Returns:
            credentials of account name that matched account name
        """
        for credential in cls.credential_list:
            if credential.account_name == password:
                return credential
