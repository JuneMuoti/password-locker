import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    A test case that defines test cases for the user class

    Args:
    unittest.Testcase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_user = User("June","Muoti","12345")
    def test_init(self):
        """
        test_init case to test of the object  is initialized properly
        """
        self.assertEqual(self.new_user.first_name,"June")
        self.assertEqual(self.new_user.last_name,"Muoti")
        self.assertEqual(self.new_user.password,"12345")
    def test_save_user(self):
        """
        test_save_user test to check if user has been saved into the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def tearDown(self):
        """
        teadown method cleans up after each test case
        """
        User.user_list = []
    def test_save_multiple_users(self):
        """
        to check if we can add multiple users to our user user_list
        """
        self.new_user.save_user()
        test_user = User("name1","name2","56789")
        test_user.save_user()
        test.assertEqual(len(User.user_list),2)



if __name__ == '__main__':
    unittest.main()
