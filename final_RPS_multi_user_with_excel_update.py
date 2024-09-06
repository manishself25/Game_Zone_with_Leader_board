######################## final RPS user 1 vs user 2 (with excel update)######################
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

def get_user1_choice(user1_name):
    choices1 = ['rock', 'paper', 'scissors']
    user1_choice = input('''Enter user 1 choice (rock, paper, scissors)
                            or
                    To Exit Enter " Q " : ''').lower()
    if user1_choice == "q":
        return user1_choice
    while user1_choice not in choices1:
        user1_choice = input(f"Invalid choice. Enter {user1_name} choice (rock, paper, scissors): ").lower()
    return user1_choice

def get_user2_choice(user2_name):
    choices2 = ['rock', 'paper', 'scissors']
    user2_choice = input('''Enter user 2 choice (rock, paper, scissors)
                            or
                    To Exit Enter " 0 " : ''').lower()
    if user2_choice == "0":
        return user2_choice
    while user2_choice not in choices2:
        user2_choice = input(f"Invalid choice. Enter {user2_name} choice (rock, paper, scissors): ").lower()
    return user2_choice

def determine_winner(user1_choice, user2_choice):
    if user1_choice == user2_choice:
        return "tie"
    elif (user1_choice == 'rock' and user2_choice == 'scissors') or (user1_choice == 'paper' and user2_choice == 'rock') or (user1_choice == 'scissors' and user2_choice == 'paper'):
        return "user1"
    else:
        return "user2"

def main(name):
    print("Welcome to Rock, Paper, Scissors!")
    # user1_name = input("Enter Player 1 Name : ").title() # ye bala username lena cheheye 
    user1_name = name
    user2_name = input("Enter username of Player 2 : ").title() # ye bala second person name manually 
    user1_score = 0
    user2_score = 0
    ties = 0

    for _ in range(5):
        user1_choice = get_user1_choice(user1_name)
        if user1_choice == "0":
            break 

        user2_choice = get_user2_choice(user2_name)
        if user2_choice == "0":
            break 
        print(f"User 1 chose: {user1_choice}")
        print(f"User 2 chose: {user2_choice}")

        result = determine_winner(user1_choice, user2_choice)
        if result == "user1":
            user1_score += 1
            print(f"congratulations {user1_name}, You win this round!")
        elif result == "user2":
            user2_score += 1
            print(f"congratulations {user2_name}, You win this round!")
        else:
            ties += 1
            print("This round is a tie!")

    print("\nFinal Scores:")
    print(f"user 1: {user1_score}")
    print(f"user 2: {user2_score}")
    print(f"Ties: {ties}")

    if user1_score > user2_score:
        score = user1_score
        finalname = user1_name
        print(f"congratulations {name}, You win the game!")
    elif user2_score > user1_score:
        score = user2_score
        finalname = user2_name
        print(f"congratulations {name}, You win the game!")
    else:
        score = ties
        finalname = "Tie"
        print("The game is a tie!")

    dtt = dt()
    ############ Excel bala kam ############################################
    df = pd.read_excel('output.xlsx')

    # Prepare the data for the new row as a dictionary
    new_row = {"Name": finalname, "Game_name": "RPS", "Current_score": score,"Date":dtt[0],"Time":dtt[1]}

    # Append the new row to the DataFrame
    df = df.append(new_row, ignore_index=True)  # ignore_index avoids duplicate row indexing

    # Save the DataFrame back to the Excel file
    df.to_excel('output.xlsx', index=False)

