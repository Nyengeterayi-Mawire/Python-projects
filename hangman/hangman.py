from pickle import TRUE
from turtle import clear
import os

def remaining(guessed): 
    count=0
    for i in guessed: 
        if i == '_':
            count += 1 
    return count


def search(answer,word_list,guessed):
   for i in range(len(word_list)):
       if word_list[i]==answer:
           guessed[i]=answer
   myString=' '.join(guessed)
   print( myString)


word = input('please enter word ')  
word_list = []
guessed= []
current=''
count=0
attempts=6  

CLEAR ='\003[2J' 
CLEAR_AND_RETURN = '\003[H]' 

print(CLEAR)


for i in range(len(word)):
    guessed.append('_') 

for i in word: 
    word_list.append(i) 

for i in range(len(word_list)): 
    if i==0 or i==len(word_list)-1: 
        guessed[i]=word_list[i]
    else: 
        guessed[i]='_'

string=' '.join(guessed)
print('word to guess is : ',string )

while count<6 and remaining(guessed)!=0:
    found=False
    print('\n')
    answer = input('please enter letter : ')
    for i in word:
        if i==answer: 
            found=True
            #search(answer,word_list,guessed)
            current= search(answer,word_list,guessed)
            print('attempts left = ',attempts)
            break

            
            
    if found==False:
        count+=1 
        attempts-=1
        search(answer,word_list,guessed)
        print('attempts left = ',attempts)
   

string = ' '.join(guessed)

if count==6 :   
    print('GAME OVER :you failed try again') 
else: 
    print('WELL DONE :you won')







