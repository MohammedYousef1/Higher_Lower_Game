from data import data
from Art import logo, vs
import random
import os
def random_account():
    """ This method retrun random data """
    return random.choice(data)

def brief_description(data):
    """ This will print breif description """
    return(f"{data['name']} , a {data['description']} , from {data['country']}.")

def compare_followers(first_data , second_data):
    """ This will return the person with more followers"""
    if(first_data['follower_count'] > second_data['follower_count']):
        return 'a'
    return 'b'

print(logo)
points = 0
account_a = random_account()
account_b = random_account()

lost = False
while(True):
    account_a = account_b
    account_b = random_account()
    while(account_a == account_b):
        account_b = random_account()
    print(f"Compare A: {brief_description(account_a)}")
    print(vs)
    print(f"Against B: {brief_description(account_b)}")

    choice = input("Enter either A or B --> ").lower()
    if(compare_followers(account_a, account_b) == choice):
        points = points + 1
    else:
        lost = True
    if(lost == True):
        break
    os.system('cls')
    print(logo)
    print(f"Thats right! Current score: {points}.")

os.system('cls')
print(logo)
print(f"You lost. Final score: {points}")