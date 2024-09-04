import random as r
import random
import pandas as pd
import datetime

# In[2]:


def passSuggest():
    import random as r
    alphaLower = 'abcdefghijklmnopqrstuvwxyz'
    alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit      = '0123456789'
    specChar   = '!@#$%^&*_-+=<>'
    
    count = [r.choice(range(2, 6)) for i in range(4)] 
    al3   = [r.choice(alphaLower)    for i in range(count[0])]
    au3   = [r.choice(alphaUpper)    for i in range(count[1])]
    d3    = [r.choice(digit)         for i in range(count[2])]
    s3    = [r.choice(specChar)      for i in range(count[3])]
    
    l = []
    for li in [al3, au3, d3, s3]:
        l.extend(li)
    r.shuffle(l)
    s = ''.join(l)
    return s


# In[3]:


def checkPasswordStength(password):
    while True:
        specChar = '!@#$%^&*_-+=<>'
        ac = uc = lc = dc = sc = 0
        strength = 0
        if len(password)>=8:
            for char in password:
                if char.isalpha():
                    ac += 1
                    if char.isupper(): uc += 1
                    else             : lc += 1
                elif char.isdigit()  : dc += 1
                elif char in specChar: sc += 1
        
            if ac > 0 and dc > 0     : strength += 1
            else                     : print('Combination of alpha and digit is a must')
            
            if uc > 0 and lc > 0     : strength += 1 
            else                     : print('Upper case and lower case of alpha is a must')
            
            if sc > 0                : strength += 1
            else                     : print('Special Character is a must')
            
            if strength == 3:
                print('password is strong')
                return password
            else:
                e = 1
        else:
            print('password should be atleast 8 characters')
            e = 1
        
        if e == 1:
                password = passSuggest()
                print(f'''Password not strong. Suggested password is {password}
                    press 0 to Exit
                    or''')
                password = input('please enter a strong password again:')
                if password == '0': return 0 


# In[11]:


def takeDetails(username):
    name = input('Enter name:').title()
    phone = input('Enter 10-digit phone number : ')
    while True:
        if len(phone) != 10:
            phone = input('''Invalid phone...
            Enter Valid 10-digit Phone Number : ''')
        else:
            break
            
    email = input('Enter Email address:').lower()
    while True:
        mail = email.split("@")
        if "gmail.com" not in mail:
            email = input('''Invalid Email...
            Enter Valid Email (With @gmail.com): ''')
        else:
            break
            
    l= [name, phone, email]
    return l


# In[12]:


def secQuestion(username):
    questionDb = ['Your first school ?','your first crush name ?']
    ans1 = input(f'Question: {questionDb[0]}').lower()
    ans2 = input(f'Question: {questionDb[1]}').lower()
    ansList = [ans1,ans2]
    return ansList


# In[13]:


def SignUp():
    global df, username_list, password_list, Ans1_list, Ans2_list
    print('************** Welcome to SignUp Portal ****************')
    
    first = 1
    while True:
        username = input('Enter a new username: ').lower().strip()
        if username == '0'and first == 0:
            print('SignUp failed....')
            return
        if username not in username_list:
            password = input('Enter a strong password: ')
            password = checkPasswordStength(password)
            if password == 0:
                print('SignUp failed....')
                return
            
            userdetail = takeDetails(username)
            secAnswer_list = secQuestion(username)
            # generateBackupCodes(username)
            print('SignUp Sucessful_ _ _')
            dtt = dt()
            new_row = {"Name": userdetail[0], "Username": username, "Password": password ,"Phone_no": userdetail[1],"Ans_1":secAnswer_list[0],"Ans_2":secAnswer_list[1],"Date":dtt[0],"Time":dtt[1],"After_5_minutes":dtt[2], "Status":"Log out"}
            # Append the new row to the DataFrame
            df = df.append(new_row, ignore_index=True)  # ignore_index avoids duplicate row indexing
            df.to_excel('Authentication_excel.xlsx', index=False)
            return
        else:
            print('''Username already taken. please try again ...
            Press 0 to Exit
            Or''')
            first = 0


# In[20]:


def forgotpassword(username):
    global df, username_list, password_list, Ans1_list, Ans2_list
    print("************** Security Question **************")
    que = ("Q1. your first school name ?","Q2. Enter your first crush name ?")
    print(que[0])
    ans1  = input("Enter ans : ").lower()
    print(que[1])
    ans2  = input("Enter ans : ").lower()
    
    if ans1 == Ans2_list[username_list.index(username)] or ans2 == Ans2_list[username_list.index(username)]:
        new_password = input('''Enter new password : ''')
        new_password = checkPasswordStength(new_password)
        username_indices = df[df['Username'] == username].index
        df.loc[username_indices[0],"Password"] = new_password
        print("************ Password update Successfully *************")
        df.to_excel('Authentication_excel.xlsx', index=False)
    else :
        print("************ Your Security Answer's are incorrect ************")


# In[21]:


def signIn_using_question(username):
    global df, username_list, password_list, Ans1_list, Ans2_list
    print("************** Security Question **************")
    que = ("Q1. your first school name ?","Q2. Enter your first crush name ?")
    print(que[0])
    ans1  = input("Enter ans : ").lower()
    print(que[1])
    ans2  = input("Enter ans : ").lower()
    
    if ans1 == Ans2_list[username_list.index(username)] or ans2 == Ans2_list[username_list.index(username)]:
        dtt = dt()
        username_indices = df[df['Username'] == username].index            
        df.loc[username_indices[0],"After_5_minutes"]=dtt[2]
        df.loc[username_indices[0],"Status"] = "Log In"
        print("************ SignIn Successfully *************")
        df.to_excel('Authentication_excel.xlsx', index=False)
    else :
        print("************ Your Security Answer's are incorrect ************")


# In[22]:


def SignIn():
    global df, username_list, password_list, Ans1_list, Ans2_list
    print('************** Welcome to SignIn Portal **************')
    
    while True:
        username = input('Enter an existing username:').lower().strip()
        if username == '0':
            print('SignIn failed')
            return
        if username == '1': SignUp()
        if username in username_list:
            for i in range(3): 
                password = input('Enter your Password: ')
                if password =="0": break
                if password =='1':
                    signIn_using_question(username)
                    return
                if password =='2':
                    forgotpassword(username)
                    return
                
                if password == password_list[username_list.index(username)]:
                    dtt = dt()
                    username_indices = df[df['Username'] == username].index
                    df.loc[username_indices[0], "After_5_minutes"] = dtt[2]
                    df.loc[username_indices[0], "Status"] = "Log In"

                    print('signIn Successful....')
                    df.to_excel('Authentication_excel.xlsx', index=False)
                    return

                
                if i == 2:
                    print('''Press 1 to SignUp for a new account
                        Press 0 to Exit
                        or''') 
                else:
                    print('''Wrong password. Please try again...
                    Press 1 to SignIn using Security Question
                    Press 2 to Forgot Password
                    Press 0 to Exit
                    or 
                    Enter option''')
        else:
            print('''Username not registered. Please try again
            Press 1 to SignUp for a new account
            Press 0 to Exit
            or''')        


            
def dt():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    date= f"{day}_{month}_{year}"
    #time= f"{hour}:{minute}"
    time = now.strftime("%H:%M")
    # Add 5 minutes to the current time
    five_minutes_from_now = now + datetime.timedelta(minutes=5)
    five_minutes_from_now = five_minutes_from_now.strftime("%H:%M")
    
    return [date, time, five_minutes_from_now]


# In[23]:




############ Excel bala kam ###############################################################
df = pd.read_excel('Authentication_excel.xlsx')
username_list = df.Username.tolist()
password_list = df.Password.tolist()
Ans1_list = df.Ans_1.tolist()
Ans2_list = df.Ans_2.tolist()

    # global df, username_list, password_list, Ans1_list, Ans2_list

def main(name):
    

    while True:
        df = pd.read_excel('Authentication_excel.xlsx')
        mode = input(''' Welcome to Authentication System
        Enter choice:
        press 1 to SignUp
        press 2 to SignIn
        Press 0 to Exit
        :''')
        if  mode == '1':
            print('SignUp....')
            SignUp()
        elif mode == '2':
            global username_list, password_list, Ans1_list, Ans2_list
            
            df = pd.read_excel('Authentication_excel.xlsx')
            username_list = df.Username.tolist()
            password_list = df.Password.tolist()
            Ans1_list = df.Ans_1.tolist()
            Ans2_list = df.Ans_2.tolist()

            
            print('SignIn....')
            #SignIn(df, username_list, password_list, Ans1_list, Ans2_list)
            SignIn()
            #break
        elif mode == '0':
            print('Thank you for visiting our website.....')
            df.to_excel('Authentication_excel.xlsx', index=False)
            break
        else:
            print('Enter valid mode')