import unittest
from user import user

class TestUser(unnittest.TestCase):
    """
    A test case that defines test cases for the user class

    Args:
    unittest.Testcase: TestCase class that helps in creating test cases
    """
    def setup(self):
        """
        Set up method to run before each test case.
        """
        self.new_user = User("June","Muoti","12345")
    def test_init(self):
        """
        test_init case to test of the object  is initialized properly
        """
        self.assertEqual(self.new_user.first_name,"June")
        self.asserEqual(self.new_user.last_name,"Muoti")
        self.assertEqual(self.new_user.password,"12345")

if __name__ == '__main__':
    unittest.main()
