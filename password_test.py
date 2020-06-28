import unittest
from password_locker import User, Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviors.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User("toni","1234","toni@gmail.com") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"toni")
        self.assertEqual(self.new_user.password,"1234")
        self.assertEqual(self.new_user.email,"toni@gmail.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_user(self):

        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","0000","tt@gmail.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test","0000","tt@gmail.com") # new user
        test_user.save_user()

        self.new_user.delete_user() # Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_display_user(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

if __name__ == '__main__':
    unittest.main()


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviors.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_credential = Credentials("instagram","toni_guthiga","1234g") # create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"instagram")
        self.assertEqual(self.new_credential.account_username,"toni_guthiga")
        self.assertEqual(self.new_credential.account_password,"1234g")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credential_list = []

    def test_save_credential(self):

        '''
        test_save_user test case to test if the credential object is saved into the credential list
        '''
        
        self.new_credential.save_credential() # saving the new account
        self.assertEqual(len(Credentials.credential_list),1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("facebook","toniguthiga","1122g") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("instagram","toni_guthiga","1234g") # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential() # Deleting a credential object
        self.assertEqual(len(Credentials.credential_list),1)

    def test_display_credential(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credential(),Credentials.credential_list)

if __name__ == '__main__':
    unittest.main()
