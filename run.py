#!/usr/bin/env python3.6
from credential import Credentials
from users import user
 def create_credential(accname,password):
     """
     function to create a new credential
     """
     new_credential = Credentials(accname,password)
     return new_credential
 def save_credential(credential):
     """
     function to save a credential
     """
     credential.save_credential()
def del_credential(credential):
    """
    Function to delete a credential
    """
    credential.delete_credential()
def find_credential(name):
    """
    Function that finds a credential by name and return the credential
    """
    return Credentals.find_by_account_name(name)
def test_display_credentials():
    """
    function to display all Credentials
    """
    return Credentials.display_credentials()
def main():
    print("Welcome to Passord Locker")
    user_name = input()
    print('\n')
    print (f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
        print("Use the following short codes : cu -create a new user ,li -log in to your account,ex -exit the contact list")
         short_code = input().lower()
         if short_code == 'cu':
             print("NEW PASSWORD LOCKER ACCOUNT")
             print("~" *10)
             print("Enter First Name")
             f_name =input()
             print ("Enter second name")
             s_name= input()
             print ("Enter password")
             p_word = input()
             print ("Confirm your password")
             confirm_password = input()
             # save_contacts(create_contact(f_name,s_name,p_word))

             print('\n')
             print(f"Congrats {f_name} ,! You have a new Password account")
             print('\n')
             print("proceed to log in to your new account")
             print("Enter account user name"):
             firstname = input()
             lastname = input()
             print("Enter password:")
             password = input()
             while  password != p_word:
                 print ("You entered incorrect password")
                 print("Enter account user name:")
                 firstname = input()
                 lastname = input()
                 print("Enter password:")
                 password = input()
             else:
                 print(f"Welcome:{firstname} to your Password locker account")
                 print ('\n')
                 print ("Select from the following choices to continue: Enter vc(to view credentials),ac(to add credential),rc(to remove credential),sc(to search credential),so(to sign out)")
                 print ('\n')
                 if choice == ac:

                         print ("Enter The Account name(eg facebook,instagram, etc):")
                         account_name = input()
                         print("Enter the account password:")
                         account_password = input()
                         save_new_credential(create_new_credential(account_name,account_password))
                         print('\n')
                         print(f"New credential {account_name} added")
                         print('\n')
                     else if choice == vc:
                         print("View all your saved credentials below:")
                         if display_credentials():
                             for credential in display_credentials():
                                 print (f"Account Name:{credential.account_name}")
                                 print(f"Account Password:{credential.account_password}")
                             else:
                                 print("You have not added any credential to your password locker account")
                             else if choice == fc:
                                 print("Enter the acccount name you want to search for in the list of credentials")
                                 find_name = input()
                                 if check_existing_credentials(find_name):
                                     search_credential = find_credential(find_name)
                                     print (f"{search_credential.account_name} {search_credential.account_password}")
                                     print('~' *20)
                                     print('\n')
                                     print (f"Account Name:{search_credential.account_name}")
                                     print(f"Account password: {search_credential.account_password}")
                                 else:
                                     print("That account does not exixt")
