#!/usr/bin/env python
# coding: utf-8

# ## Create a python program that generates 3 digit random passcode for users. Authenticate if the passcodes generated match the user's input. 

# In[2]:


import random


# In[3]:


new = [' ',' ',' ']
def check():
    for i in range(1):
        if new[0] == ' ':
            new[0] = user
            break
        if new[1] == ' ':
            new[1] = user
            break
        if new[2] == ' ':
            new[2] = user
            break

def authentication():
    if new[0] == passcode[0] and new[1] == passcode[1] and new[2]==passcode[2 ]:
        print('Account creation successful')
    else:
        print('Wrong passcode, try again')
        
print('enter the passcode')

def display():
    print('[',new[0], '|' , new[1], '|', new[2], ']')
    
passcode = random.sample(range(90),3)
print(f'Your passcode is {passcode}')
display()
counter = 0
while True:
    try:
        while counter<3:
            user = int(input('enter the passcode: '))
            counter = counter + 1
            check()
            display()
        authentication()
        break
        
    except ValueError:
        print('invalid input, check the passcode and try again')



#                                          Random modules
# 1) random.random() ; used for floats 
# 2) random.randint(start, end) ; used to select a random number within an integer
# 3) random.choice() ; used to select a random number within a list
# 4) random.randrange ; used to return a particular number within a range
# 5) random.choices() ; used to return a list with a random selection from the given sequence
# 6) random.sample(()number_needed)) ; used to generate a list of random numbers. 
# 7) random.shuffle() ; used to shuffle between a list

# In[ ]:




