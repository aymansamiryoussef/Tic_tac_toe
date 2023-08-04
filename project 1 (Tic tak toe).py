#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=["-","-","-",
  "-","-","-",
    "-","-","-"]


# In[2]:


cur_player="X"
winner="none"
running=True


# In[3]:


def print_game(l):
    for i in range(0,8,3):
        print(l[i],"|",l[i+1],"|",l[i+2],"|"+"\n")
       


# In[4]:


def move(l):
    p=int(input("Enter number 1-9: "))
    if p>=1 and p<=9 and l[p-1]=="-":
             l[p-1]=cur_player
    else:
             print("error")
               


# In[5]:


def win (l):
        global winner
        if l[0] == l[1] == l[2] and l[0]!="-":
            winner==l[0]
            return True
    
        elif l[3] == l[4] == l[5]and l[3]!="-":
            winner==l[3]
            return True
        
        elif l[6] == l[7] == l[8]!="-"and l[6]!="-":
            winner==l[6]
            return True
            


        elif l[0] == l[3] == l[6] and l[0]!="-":
            winner==l[0]
            return True
            
        elif l[1] == l[4] == l[7] and l[1]!="-":
            winner==l[1]
            return True
            
        elif l[2] == l[5] == l[8] and l[2]!="-":
            winner==l[2]
            return True
            


        elif l[0]== l[4]==l[8] and l[0]!="-":
            winner==l[0]
            return True
            
        elif l[2] == l[4]==l[6]and l[2]!="-":
            winner==l[2]
            return True
            


        


# In[11]:


def check():
    global running
    if win(l):
        print_game(l)
        print("the winner : {} "+ winner)
        running=False


# In[12]:


def clear(l):
    for i in range (0,9):
        l[i]='-'


# In[13]:


def tie (l):
    global running
    if "-" not in l:
        print_game(l)
        print("tie")
        running=False
            


# In[14]:


def switch_players():
    global cur_player
    if cur_player=="X":
        cur_player="O"
    else:
        cur_player="X"


# In[15]:


while running:
    print_game(l)
    move(l)
    check()
    tie(l)
    switch_players()


# In[13]:





# In[ ]:




