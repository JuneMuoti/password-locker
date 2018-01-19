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
