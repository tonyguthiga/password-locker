#!/usr/bin/env python3.6
from password_locker import User, Credentials

def create_user(user_name,password,email):
    '''
    Function to create a new user
    '''

    new_user = User(user_name,password,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''

    user.save_user()

def display_users():
    '''
    Function to return all the saved users
    '''
    return User.display_users()

def login_user(user_name,password):
    '''
    Function to see if user exist and allow them to login
    '''

    check_user_exist = Credentials.check_user_exist(user_name,password)
    return check_user_exist

def create_credential(account_name,account_username,account_password):
    '''
    Function to create a new credential
    '''

    new_credential = Credentials(account_name,account_username,account_password)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''

    credential.save_credential()

def display_credential():
    '''
    Function to return all saved credentials
    '''

    return Credentials.display_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''

    credential.delete_credential()

def generate_password():
    '''
    Function that generates random password.
    '''

    password_gen = Credentials.generate_password()

    return password_gen

def main():
    print("Hello Welcome to your Password locker!")
    print('\n')
    while True:
        print("Use these short codes : nu - create a new user account, ln - login to your account, du - display users, et - exit password locker")

        short_code = input().lower()

        if short_code == "et":
            print("Thank you for you time, Bye...")
            break

        elif short_code == "nu":
            print("Sign Up")
            print('-' * 30)
            
            user_name = input("user_name: ")
            password = input("password: ")
            email = input("email: ")

            save_users(create_user(user_name,password,email))
            print('\n')

            print(f"Hello,{user_name} Your account was successfully been created")
            print('\n')
            print('-' * 30)

        elif short_code == "du":
            if display_users():
                print("List of users:")
                print('\n')
                for user in display_users():
                    print(f"{user.user_name}")
                    print('\n')

        elif short_code == "ln":
            print("Enter your username and password to log in:")
            print('-' * 30)

            user_name = input("User name: ")
            password = input("password: ")
            sign_in = login_user(user_name,password)
            if sign_in == True:
                print(f"Hello,{user_name} select an option.")
                while True:
                    print('-' * 60)
                    short_code = input("Codes: ca - create an account or name of site, dc - display the list of your credentials, ex - exit site \n").lower().strip()
                    print('-' * 60)
                    if short_code == "ca":
                        print("Create new account")
                        print('-' * 30)
                        account_name = input("Account/site name: ")
                        account_username = input("Site user name: ")
                        print('-' * 60)
                        password_option = input("Select one option: (ep-enter existing password or (gp-generate password) \n").strip()
                        print('-' * 60)
                        while True:
                            if password_option == "ep":
                                account_password = input("Enter your password: 8 characters minimum: ")
                                break
                            elif password_option == "gp":
                                account_password = generate_password()
                                break
                            else:
                                print("Invalid")
                                break
                        save_credential(create_credential(account_username,account_username,account_password))
                        print('-' * 30)
                        print(f"New created account: \n Account:{account_name}\n User Name:{account_username} \n Password: {account_password}")
                        print('-' * 30)

                    elif short_code == "dc":
                        if display_credential():
                            print("Here is your account list: ")

                            print('-' * 30)
                            for account in display_credential():
                                print(f"Site:{account.account_name} \n User Name:{account_username} \n Password:{account_password}")
                                print('-' * 30)
                            print('#' * 30)
                        else:
                            print("Sorry, you dont have any accounts")

                    elif short_code == "ex":
                        print("Bye...")
                        break
                    else:
                        print("Invalid")

    else :
        print("Inorder to proceed you have to create an account:")


if __name__ == '__main__':
    main()

