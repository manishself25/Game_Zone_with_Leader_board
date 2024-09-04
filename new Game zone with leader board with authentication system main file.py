#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
print('''Welcome to Game Zone of Manish''')
a = True
statusInfo = 0

while a:
    try:
        df = pd.read_excel('Authentication_excel.xlsx')
    except FileNotFoundError:
        print(f"Error: The file 'Authentication_excel' was not found.")
        print("Creating a new file with default structure...")

        data = {
            "Name":[],
            'Username': [],
            "Password": [],
            "Phone_no": [],
            "Ans_1": [],
            "Ans_2": [],
            "Date": [],
            "Time": [],
            "Status": []
        }
    
        df = pd.DataFrame(data)
        df.to_excel("Authentication_excel.xlsx", index=False)
        print(f"New file 'Authentication_excel.xlsx' created successfully.")
    
    user = input("Enter User Name : ").strip()
    if user == "0":
        print("Thankyou for visiting.....")
        a = False
        break 
    
    if user in df["Username"].tolist():
        print(1)
        username_indices = df[df['Username'] == user].index
        statusInfo = df.iloc[username_indices[0],8]
        timeinfo = df.iloc[username_indices[0],7]
        timeinfo_after = df.iloc[username_indices[0],9]

    if statusInfo == "Log In" :#and (timeinfo_after.hour > timeinfo.hour or (timeinfo_after.hour == timeinfo.hour and timeinfo_after.minute > timeinfo.minute)):
        print(2)
        b = True
        while b:
            x = input('''Press 1 to Play KBC
            Press 2 to Tic Tac Toe
            Press 3 to Play Hangman
            Press 4 to Rock Paper Scissors with computer
            Press 5 to multi user Rock Paper Scissors
            Press 6 to Check Leader board
                   or 
            To Exit Press 0
            Enter your choice : ''')

            if x == "1":
                import kbc_with_level_excel_update as game1
                game1.main(user)
            elif x == "2":
                print("Try after some time")
            elif x == "3":
                import final_hangman_with_excel_update as game3
                game3.main(user)
            elif x == "4":
                import final_RPS_game_user_vs_computer_with_excel_update as game4
                game4.main(user)
            elif x == "5":
                import final_RPS_multi_user_with_excel_update as game5
                game5.main(user)
            elif x == "6":
                import Leader_board_final
            elif x == "0":
                print("Thankyou ..... GAME OVER")
                a = False
                b = False
            else:
                print("Enter Valid Option")
                
    elif statusInfo == "Log out":
        print("Complete signin process ----->>")
        try:
            import ASNEW_DONE as ase1
            ase1.main(user)
        except ImportError:
            print("Error: ASNEW_DONE module is missing or failed to import.")
        
        
    else :
        print('''Error * 
        Username not SignIn or Not Exist''')
        try:
            import ASNEW_DONE as ase1
            ase1.main(user)
        except ImportError:
            print("Error: ASNEW_DONE module is missing or failed to import.")


# In[6]:


df


# In[ ]:




