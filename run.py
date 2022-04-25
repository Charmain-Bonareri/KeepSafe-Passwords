#!/usr/bin/env python3.8
from user import User, Credential
import random
import string
from random import randint


def create_user(username, email, password):
    """
    Function to create a new user
    """
    new_user = User(username, email, password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def create_credential(username, phone_number, email, password):
    """
    Function to create new user credentials
    """
    new_credential = Credential(username, phone_number, email, password)
    return new_credential

def save_userInfo(credential):
    """
    Function to save Credentials to the credentials list
    """
    credential.save_userInfo()

def delete_passwords(credential):
    """
    Function to delete a Credentials from credentials list

    """
    credential.delete_passwords()

def find_by_number(number):
    """
    Function that finds passwords by number and returns the details 
    """
    return Credential.find_by_number(number)

def passwords_exist(number):
    """
    Function that check if a passwords exists with that number return true or false

    """
    return Credential.passwords_exist(number)

def display_passwords():
    """
    Function that returns all the saved passwords
    """
    return Credential.display_passwords()

'''
This a function to generate random password
'''
def get_random_password():
    password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(*&^%$#@!)"
    ran=len(password)
    randomPassword=''
    for i in range(6):
        all=password[random.randint(0,ran)]
        randomPassword=randomPassword+all
    return randomPassword


def main():  
        print("Welcome to KeepSafePasswords, I hope your are having a fantastic day! What is your name?")        
        name=input()
        print("Which account are you saving its details?")
        KeepSafeAccount=input()
        print(f"Hey {name}, please enter your username")
        username=input()
        print(f"{name}, please enter your phone number")
        phone_number = input()
        print(f"{name}, please enter your email")
        email = input()
        print("Please choose between the following options: gp-generate password or mp- to make your own password ")
        short_codes=input().lower()
        if short_codes=="gp":            
            print('\n')
            print("~~"*40)
            password=get_random_password()
           
            print("Yaay! your details have been saved successfully!")
            print("~~"*40)
            print("Your username is " +username +" and your password is "+password)
            print("~~"*40)
        else:
            print("Enter your password")           
            password=input()  
            print("~~"*40)
            print("Your username is " +username +" and your password is "+password)
            print("~~"*40)      
        save_userInfo(Credential(KeepSafeAccount, username,phone_number, email, password))
        print("\n")
        print(f"Welcome to your KeepSafe account {name}")
        while True:
                print("Please choose between the following options\n cp-- create new password details  dp-- display saved password details  fp-- find a specific details by number   da-- delete password details ex-- exit KeepSafePasswords ")
                short_codes=input().lower()
                if short_codes=="cp":
                    print("-"*10)
                    print("Time to create your new account details\n")
                    print(f"{name} please enter the account name you are creating details for i.e., Snapchat, Twitter, Workday, Jumia")
                    KeepSafeAccount=input();
                    print("please enter your preferred username")
                    username=input();
                    print(f"{name}, please enter your phone number")
                    phone_number = input()
                    print("please enter your password")
                    password=input()
                    save_userInfo(Credential(KeepSafeAccount, username,phone_number, email, password))
                    print("\n")
                    print("~~"*40)
                    print(f"KeepSafe has saved your {KeepSafeAccount} account details successfully")
                    print("~~"*40)
                    print("\n")

                elif short_codes=="dp":
                    if display_passwords():
                        print(f"{name} This is a list of all your details")
                        print("--"*40)                       
                       
                        for details in display_passwords():
                            print(f"Account Details:{KeepSafeAccount} \n User Name:{username}\n Phone number:{phone_number}\n  Email:{email}\n Password:{password}")
                            print("\n")
                        print("--"*40)
                    else:
                        print("\n")
                        print("Don't worry, you might not have saved password details yet") 

                elif short_codes=="fp":
                    print("please enter the phone number of the account")
                    find_pass=input();
                    if find_by_number(find_pass):
                        searchPasswords=find_by_number(find_pass)
                        print("\n")                        
                        print("Username\t password")
                        print("__"*40)
                        print(f"{searchPasswords.password}...\t{searchPasswords.email}")
                        print("__"*40)
                        print("\n")
                    else:
                        print("Ooops! Sorry,that Account does not exist. Please try again")
                        print("__"*40)
                        print("\n")

                elif short_codes=="da":
                    print("You are about to delete your password details. Enter the name of the account")
                    delAccount=input();
                    if passwords_exist(delAccount):
                        for password in delete_passwords :
                          Credential.remove(Credential)
                          delete_passwords = [i for i in delAccount if i in Credential]
                          Credential.remove(delete_passwords [0])
                        print('Your password for ' + str(delAccount) + ' has been successfully removed.')
                        print("\n")
                    else:
                        print("Don't worry, it seems an error occured, perhaps those password details does not exist")
                        print("\n")

                elif short_codes=="ex":
                        print("We are sad to see you leave! .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")

                            



if __name__ == '__main__':
       main()