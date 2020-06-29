import string
import random

class User:
    '''
    class that generates new instances of users.
    '''

    user_list = []

    def __init__(self,user_name,password,email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved contact from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that return the contact list
        '''
        return cls.user_list



class Credentials:
    '''
    class that generates new instances of credentials.
    '''

    credential_list = []

    def __init__(self,account_name,account_username,account_password):
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''
        Credentials.credential_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def display_credential(cls):
        '''
        method that return the credential list
        '''
        return cls.credential_list

    @classmethod
    def check_user_exist(cls,user_name,password):
        '''
        method that check if a user exist from user list
        '''

        for user in User.user_list:
            if user.user_name == user_name and user.password == password:
                return True
            return False 
    @classmethod
    def generate_password(size = 8,char = string.ascii_letters + string.digits + string.punctuation):
        
        gen_pass = "".join(random.choice(char) for _ in range(8))
        return gen_pass