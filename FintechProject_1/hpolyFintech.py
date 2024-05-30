"""
This is a basic fintech application with very basic functionalities using the console.
We will implement this using basic functions rather than classes.
however, this code shall be improved upon in later days.

The application shall contain the following basic features:
1. User Registration
2. Account Number generation
3. Deposit and Withdrawal feature
    For the withdrawal, we shall further have the below features
    1. Transfer
    2. Buy Airtime
    3. Data subscription
4. Check balance
5. Retrieve Account Number

INSTRUCTIONS: You are not allowed to delete any code written here rather, update the part with the # to perform the
expected output, ensure to test your codes progressively
"""
import json
from json import JSONDecodeError
from random import randint


withdrawal_type = {
    1: "transfer",
    2: "Airtime purchase",
    3: "Data Subscription"
}

def accountData():
    """
    This function returns account data
    :return: json
    """
    try:
        with open("accountData.json", "r") as file:
            data = json.load(file)
        return data
    except JSONDecodeError:
        return

def update_amount(accountNumber, amount, sign):
    """
    This function will update the amount of a user based on deposit and withdrawal
    :param accountNumber:
    :param amount:
    :return:
    """
    available_data = accountData()
    if available_data:
        for content in available_data:
            if accountNumber == content["accountNumber"]:
                if sign == "+":
                    content["amount"] += amount
                elif sign == "-":
                    content["amount"] -= amount
                with open("accountData.json", "r") as file:
                    json.dump(available_data, file)
                return content["amount"]
def save_amount(accountNumber, amount, sign="+"):
    update_amount(accountNumber, amount, sign)

def deduct_amount(accountNumber, amount, sign="-"):
    update_amount(accountNumber, amount, sign)


def user_registration(*args, **kwargs):
    """
    A user is expected to pass the following details for registration
    1. userName as username
    2. 4 digit pin for withdrawal as pin
    3. age as age
    4. initial deposit as amount,
    :param args: this will not be useful for this project
    :param kwargs: collect user data and pass to kwargs.
    :return: returns user registration data
    """

    userData = {}
    # collect the data from user and store it to the above defined dictionary,

    """
    Follow the example used to validate the age below for the above requirement
    """

    if kwargs["age"] < 18:
        userData["tier"] = 1
    else:
        userData["tier"] = 2
    userData["accountNumber"] = generateAccountNumber()

    initialData = accountData() or []
    initialData.append(userData)

    with open("accountData.json", "w") as file:
        json.dump(initialData, file)

def generateAccountNumber():
    """
    This function generate a random account number of 10 digits
    while ensuring that the account is unique in the json data
    :return: int
    """
    while True:
        accountNumber = randint(2000000000, 2999999999)
        validataExistence = accountData()
        if validataExistence:
            if accountNumber not in validataExistence[0]:
                return accountNumber
        else:
            return accountNumber

def deposit(username, accountNumber):
    """
    Update the user account number and print its current balance
    :param username:
    :param accountNumber:
    :return: int
    """

    # confirm if the username and accountNumber passed to this function exists in accountData() defined above
    ## if it exist, ask user to enter an amount else return Invalid Account details
    ### using the new amount, add to the user existing record and print the balance to the user
    #### return a message for the user exactly as seen below
    """
    deposit alert:
    Hello username, your account has be credited with {deposit amount},
    Your new account balance is {account balance}
    """

def get_account_number(username, pin):
    """
    Define a function to get user account number
    :param username:
    :param pin:
    :return:
    """
    # This is a simple function, get username and pin from user, if they match what we have in the json file,
    # return user account number with the message
    """
    Hello username:
    Your account number is {account Number}
    """

def check_balance(username, pin):
    """
    Define a function to return user balance to the user
    :param username:
    :param pin:
    :return: float
    """
    # This is a simple function, get username and pin from user, if they match what we have in the json file,
    # return user account balance with the message
    """
    Hello username:
    Your account balance is {account balance}
    """

def withdrawals(accountNumber, pin):
    """
    Define a means to withdraw funds either by transfer, purchase airtime or data subscription
    :param accountNumber:
    :param pin:
    :return:
    """
    # validate if accountNumber and pin exist, if yes, define an input to get withdrawal type
    # refer to the withdrawal_type above for its content
    ## if a user pass an integer higher or lesser than the defined keys, return Invalid option and allow multiple trials

    ### if user selection is 1, ask for recipient account number, validate to ensure its 10 digits else return
    ### invalid account information, at the moment we wont be looking at bankName until next project

    #### if account number is validated, collect amount to be tranferred,

    ##### validate if user account balance is up to the transferred amount, if yes, return successful transaction
    ##### and deduct amount from user account balance, hence return the following message

    """
    Hello username:
    You have successfully transferred {transfer amount} to {recepient accountNumber}
    Your current balance is {user current balance after deduction}
    """

    ###### for the data and airtime, on selection, return service not available at the moment, we will look out for
    ###### this in the next phase of this project

    """
    Note: You are free to add your own creativity to this project but ensure that all the above listed criteria are meet
    You should only use print statement to test your code within any function defined above, before submission, ensure
    that you are using only the return statement within all functions defined in this file.
    Lastly, do not leave any function executed in this function, all the functions will be called on the run.py file
    
    Reach out to me if you need further clarity or encounter any challenge.
    """

