import unittest
from credential import Credentials

class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours
    """
    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_credential = Credentials("facebook","67893")
    def test_init(self):
        """
        test_init case to test if the object is initialized
        """
        self.assertEqual(self.new_credential.account_name,"facebook")
        self.assertEqual(self.new_credential.account_password,"67893")
    def tearDown(self):
        """
        Teardown does clean up after each test case has run
        """
        Credentials.credential_list = []
    def test_save_credential(self):
        """
        To test if a given credential is saved into the credentials list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)
    def test_save_multiple_credentials(self):
         """
         to check if we can save multiple accounts to our credential list
         """
         self.new_credential.save_credential()
         test_credential = Credentials("account","password")
         test_credential.save_credential()
         self.assertEqual(len(Credentials.credential_list),2)
    def test_delete_credential(self):
        """
        to test if we can remove a given credential from the list of credentials
        """
        self.new_credential.save_credential()
        test_credential = Credentials("facebook","56789")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_list),1)
    def test_find_credential_by_account_name(self):
        """
        test to check if we can find a credential by its account name and display info
        """
        self.new_credential.save_credential()
        test_credential = Credentials("facebook","password")
        test_credential.save_credential()
        found_credential = Credentials.find_by_account_name("facebook")
        self.assertEqual(found_contact.password,test_credential.password)




if __name__ == '__main__':
    unittest.main()
