#!/usr/bin/env python
# coding: utf-8

# In[1]:


######################## final RPS computer vs user (with excel update)######################
import random
import pandas as pd
import datetime

def dt():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    date= f"{day}_{month}_{year}"
    time= f"{hour}:{minute}"
    return [date,time]

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input('''Enter your choice (rock, paper, scissors)
                            or
                    To Exit Enter " Q " : ''').lower()
    if user_choice == "q":
        return user_choice
    while user_choice not in choices:
        user_choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or        (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"


def main(name):
    print("Welcome to Rock, Paper, Scissors!")
    # name = input("Enter Your Name : ").title()
    user_score = 0
    computer_score = 0
    ties = 0

    for _ in range(5):
        user_choice = get_user_choice()
        if user_choice == "q":
            break 
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            user_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            ties += 1
            print("This round is a tie!")

    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")

    if user_score > computer_score:
        score = user_score
        print(f"congratulations {name}, You win the game!")
    elif computer_score > user_score:
        name  = "Computer"
        score = computer_score
        print("Computer wins the game!")
    else:
        name = "Tie"
        score = ties
        print("The game is a tie!")

    dtt = dt()
    ############ Excel bala kam ############################################
    df = pd.read_excel('output.xlsx')

    # Prepare the data for the new row as a dictionary
    new_row = {"Name": name, "Game_name": "RPS", "Current_score": score,"Date":dtt[0],"Time":dtt[1]}

    # Append the new row to the DataFrame
    df = df.append(new_row, ignore_index=True)  # ignore_index avoids duplicate row indexing

    # Save the DataFrame back to the Excel file
    df.to_excel('output.xlsx', index=False)