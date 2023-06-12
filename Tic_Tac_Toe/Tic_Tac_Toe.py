import random
def frame(player1,player2):
    for i in range(5): 
        #print('\n') 
        if i==1 or i==3:          
            for k in range(11): 
                    print('-',end='') 
            print()
        else:      
            for j in range(11): 
                s=False
                if j==3 or j==7: 
                    print('|',end='') 
                elif j==1 or j==1 or j==2 or j==4 or j==5 or j==6 or j==8 or j==9 or j==0: 
                    #print(' ',end='')
                    if j==1 or j==5 or j==9: 
                        #print('-',end='') 
                        for l in player1: 
                            if l=='ul' and i==0 and j==1:
                                            print('x',end='')
                                            s=True
                            elif l=='um' and i==0 and j==5:
                                            print('x',end='')
                                            s=True
                            elif l=='ur' and i==0 and j==9:
                                            print('x',end='')
                                            s=True
                            elif l=='ml' and i==2 and j==1:
                                            print('x',end='')
                                            s=True
                            elif l=='mm' and i==2 and j==5:
                                            print('x',end='')
                                            s=True
                            elif l=='mr' and i==2 and j==9:
                                            print('x',end='')
                                            s=True
                            elif l=='ll' and i==4 and j==1:
                                            print('x',end='')
                                            s=True
                            elif l=='lm' and i==4 and j==5:
                                            print('x',end='')
                                            s=True
                            elif l=='lr' and i==4 and j==9:
                                            print('x',end='') 
                                            s=True
                            
                        #print()                    

                        for m in player2: 
                            if m=='ul' and i==0 and j==1:
                                            print('o',end='') 
                                            s=True
                            elif m=='um' and i==0 and j==5:
                                            print('o',end='')
                                            s=True
                            elif m=='ur' and i==0 and j==9:
                                            print('o',end='')
                                            s=True
                            elif m=='ml' and i==2 and j==1:
                                            print('o',end='')
                                            s=True
                            elif m=='mm' and i==2 and j==5:
                                            print('o',end='')
                                            s=True
                            elif m=='mr' and i==2 and j==9:
                                            print('o',end='')
                                            s=True
                            elif m=='ll' and i==4 and j==1:
                                            print('o',end='')
                                            s=True
                            elif m=='lm' and i==4 and j==5:
                                            print('o',end='')
                                            s=True
                            elif m=='lr' and i==4 and j==9:
                                            print('o',end='')
                                            s=True
                        if s==False: 
                            print(' ',end='')
                        #print() 
                        #print(' ',end='')
                    else:
                        print(' ',end='')                                              
                        
            print()
      
                

def input_test(move,possible,player1,player2):
    for i in possible:
        s=True
        if move==i: 
            for j in player1: 
                if move==j: 
                    print('move has been played already by player1') 
                    s=False
            for k in player2:             
                if move==k: 
                    print('move impossible already played...please enter unused move') 
                    s=False
            return s  

def win_rule(win,Player1,Player2): 
    s=False
    for i in win: 
        P1_count=0
        for j in i: 
            for k in Player1:
                if j==k: 
                    P1_count+=1 
        if P1_count==3: 
            print('player1 has won the game')
            s=True

    for i in win: 
        P2_count=0
        for j in i: 
            for k in Player2:
                if j==k: 
                    P2_count+=1 
        if P2_count==3: 
            print('player2 has won the game')
            s=True 
    return s



#def move_postion
    

#Player1_name=input('player1 please enter name : ')
#Player2_name=input('player2 please enter name : ')
def multiplayer():
    Player1=['1']
    Player2=['1']  
    possible=['ul','um','ur','ml','mm','mr','ll','lm','lr'] 
    win=[['ul','um','ur'],['ul','ml','ll'],['ll','lm','lr'],['ur','mr','lr'],['ul','mm','lr'],['ur','mm','ll'],['ml','mm','mr'],['um','mm','lm']]
    count=0

    frame(Player1,Player2)

    #print(frame(Player1,Player2)) 
    while count<9:
        while True:
            move_test=False
            Player1_move=input('player1_name your move : ') 
            move_test=input_test(Player1_move,possible,Player1,Player2)
            if move_test==True: 
                Player1.append(Player1_move)
                count+=1
                break 
        print(frame(Player1,Player2)) 
        #print(win_rule(win,Player1,Player2))
        ctr=win_rule(win,Player1,Player2)
        if ctr==True: 
            break
        #print(win_rule(win,Player1,Player2))
        while True: 
            move_test=False
            Player2_move=input('player2_name your move : ') 
            move_test=input_test(Player2_move,possible,Player1,Player2)
            if move_test==True: 
                Player2.append(Player2_move)
                count+=1
                break 
        print(frame(Player1,Player2))
        #print(win_rule(win,Player1,Player2))
        ctr=win_rule(win,Player1,Player2)
        if ctr==True: 
            break
         
def single_palyer(): 
    Player1=['1']
    Player2=['1']  
    possible=['ul','um','ur','ml','mm','mr','ll','lm','lr'] 
    win=[['ul','um','ur'],['ul','ml','ll'],['ll','lm','lr'],['ur','mr','lr'],['ul','mm','lr'],['ur','mm','ll'],['ml','mm','mr'],['um','mm','lm']]
    count=0

    frame(Player1,Player2)

    #print(frame(Player1,Player2)) 
    while count<9:
        while True:
            move_test=False
            Player1_move=input('player1_name your move : ') 
            move_test=input_test(Player1_move,possible,Player1,Player2)
            if move_test==True: 
                Player1.append(Player1_move)
                count+=1
                break 
        print(frame(Player1,Player2)) 
        #print(win_rule(win,Player1,Player2))
        ctr=win_rule(win,Player1,Player2)
        if ctr==True: 
            break
        #print(win_rule(win,Player1,Player2))
        while True: 
            move_test=False
            Player2_move=random.sample(possible,1) 
            move_test=input_test(Player2_move,possible,Player1,Player2)
            if move_test==True: 
                Player2.append(Player2_move)
                count+=1
                break 
        print(frame(Player1,Player2))
        #print(win_rule(win,Player1,Player2))
        ctr=win_rule(win,Player1,Player2)
        if ctr==True: 
            break 

user=int(input('please enter wanted game mode - 1 for single player or 2 for multiplayer ---> '))  
if user== 1 :
    single_palyer()
elif user== 2 : 
    multiplayer()
      




    



