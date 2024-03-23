
#This tool generates potential passwords using user-specific data like:

#       usernames, surnames, pet name, and birth date. 

#===================================================================

import pyfiglet 
import string 
import os 

banner = pyfiglet.figlet_format(" Custom Password List Generator ")
print ( '\033[91m' + banner + '\033[0m')

#===================================================================

def init_parm():
    
    username=input("Username = ")
    Surname=input("Surname = ")
    pet=input("pet's name = ")
    date=input("birth date = ")
    
    return( username, Surname , pet , date)
    
#===================================================================

def add_spec_char(par1):
    spec_chars=string.punctuation
    l=[]
    for nb in par1:
        for ch in spec_chars:
            l.append(nb+ch)
    return ( l )

#===================================================================

def create_list_of_subsequence(word):
    name=[]
    for i in range ( len (word)-1):
        name.append(word[i])
        for j in range (i+1 ,  len (word)) :
            name.append( name[-1] + word[j] )
    name.append( word[-1] )
    return( name )

#===================================================================

def create_list_of_2_names(word1,word2):

    output=[]
    l1=create_list_of_subsequence(word1)[:len(word1)]
    l2=create_list_of_subsequence(word2)[:len(word2)]
    for ch1 in l1:
        for ch2 in l2:
            output.append(ch1+ch2)

    return( output)


# main prog 

( username, Surname , pet , date)=init_parm()

numbers=['9']
for i in range(9):
        numbers.append (str(i))
        for j in range ( i+1 , 10):
            numbers.append(numbers[-1]+str(j))

num=add_spec_char(numbers)

if date!="":
    num+=add_spec_char(create_list_of_subsequence(date)[:len(date)])

liste=[]
if username!="":
    liste+= create_list_of_subsequence(username)
if Surname!="":
    liste+= create_list_of_subsequence(Surname)
if pet!="":
    liste+= create_list_of_subsequence(pet)
if (username!="") and (Surname!=""):
    liste+= create_list_of_2_names(username,Surname)

line=0
with open ( os.path.abspath(os.path.dirname(__file__)) + "\\wordlist.txt" ,"w") as f :
    for ch in liste:
        for nb in num:
            if len ( ch+nb)>=6:
                f.write(ch.title()+nb+'\n')
                line+=1
f.close()

print( "wordlist created with {} lines ".format(line))                        