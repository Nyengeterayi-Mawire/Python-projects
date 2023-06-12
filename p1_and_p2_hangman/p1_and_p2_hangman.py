import csv
import random
words=[]

def single_player():
    word = input('please enter word ')  
    return word

def multiplayer():
    word=''
    with open('Aword.csv') as csv_file: 
        csv_reader = csv.reader(csv_file)    
        for row in csv_reader:  
            words.append(row) 

    p2=random.sample(words,1) 

    for i in p2: 
        for k in i:
             word=k 
    return word

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

game_type=int(input('please select game mode. Input "1" for Single Player or "2" for Multiplayer : ')) 
if game_type==1: 
    word = single_player()
elif game_type==2: 
    word= multiplayer()

   
word_list = []
guessed= []
current=''
count=0
attempts=6  


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
    print('\n GAME OVER :you failed try again') 
    print('The word was',word)
else: 
    print('WELL DONE :you won')

#print(words)
#print(random.sample(words,1))

