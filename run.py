#!/usr/bin/env python3.8
from user import User, Credential
import random

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
def random_password(limit):
    password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(*&^%$#@!)"
    ran=len(password)
    hold=''
    for i in range(0,limit):
        all=password[random.randint(0,ran)]
        hold=hold+all
    return hold