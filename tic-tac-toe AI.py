import time
import random
import itertools
winset=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
userlist=[]
systemlist=[]
corners=[0,2,6,8]
corners1=corners[:]
center=4
sides=[1,3,5,7]
sides1=sides[:]
winsubset=[]
win=0
sumofwinsetlists=[]*24
board=[int(i) for i in range(0,9)]
remaining=board[:]
placetomark=0
placetomark1=0
found=0
lst=[]
'''function to start playing game'''
def start_game():
    winset=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    board=[0,1,2,3,4,5,6,7,8]
    c1=0
    global win
    for j in winset:
        for i in itertools.combinations(j,2):
            winsubset.append(i)
    for i in winset:
        sumofwinset=sum(i)
        for j in range(3):
            sumofwinsetlists.insert(c1,sumofwinset)
            c1+=1
    while(True):
        choice=input("X or O : ")
        if choice=="X":
            time.sleep(1)
            display_board(board)
            while(isgamewin!=True):
                play_user('X')
                time.sleep(1)
                display_board(board)
                if isgamewinuser():
                    print("USER WINS")
                    win=1
                    break
                play_system('O')
                time.sleep(1)
                display_board(board)
                if isgamewin()==True:
                    time.sleep(1)
                    print("SYSTEM WINS")
                    win=1
                    break
                if len(remaining)==0:
                    print("GAME IS OVER")
                    win=1
                    break
        elif choice=="O":
            time.sleep(1)
            display_board(board)
            while(isgamewin!=True):
                play_user('O')
                if isgamewinuser():
                    print("USER WINS")
                    win=1
                    break
                play_system('X')
                time.sleep(1)
                display_board(board)
                if isgamewin():
                    time.sleep(1)
                    print("SYSTEM WINS")
                    win=1
                    break
                if len(remaining)==0:
                    print("GAME IS OVER")
                    win=1
                    break
        if win==1:
            break
'''function to display board'''
def display_board(lst):
    c=0
    for i in range(3):
        for j in range(3):
            print("-",board[c],"-",end='|')
            c+=1
        print("\n")
'''function for user playing game'''
def play_user(x):
    global userlist
    global board
    global systemlist
    global corners1
    global sides1
    place=int(input("enter a position for placing: "))
    if place not in systemlist:
        if place not in userlist:
            userlist.append(place)
            userlist=sorted(userlist)
            remaining.remove(place)
            board[place]=x
            if place in corners1:
                corners1.remove(place)
            if place in sides1:
                sides1.remove(place)
        else:
            print("already used")
            play_user(x)
    else:
        print("already used")
        play_user(x)
    for i in itertools.combinations(userlist,3):
        if i in winset:
            print("user won game")
            win=1
            break
'''function for system playing game'''
def play_system(y):
    global userlist
    global systemlist
    global board
    global win
    global remaining
    if is_system_wins():
        c=is_system_wins()
        if c in remaining:
            if c in corners1:
                corners1.remove(c)
                systemlist.append(c)
                systemlist=sorted(systemlist)
                remaining.remove(c)
                board[c]=y
                print("system selected pos: ",c)
                if isgamewin():
                    print("system is winner")
                    win=1
            if c in sides1:
                sides1.remove(c)
                systemlist.append(c)
                systemlist=sorted(systemlist)
                remaining.remove(c)
                board[c]=y
                print("system selected pos: ",c)
                if isgamewin():
                    print("system is winner")
                    win=1
        else:
            pass
    elif is_system_lose() :
        c2=is_system_lose()
        systemlist.append(c2)
        systemlist=sorted(systemlist)
        remaining.remove(c2)
        board[c2]=y
        print("system selected pos: ",c2)
    elif is_center_available():
        systemlist.append(center)
        systemlist=sorted(systemlist)
        remaining.remove(center)
        board[center]=y
        print("system selected pos: ",center)
    elif (len(corners1)>0):
        for i in corners:
            if i in remaining:
                corners1.remove(i)
                systemlist.append(i)
                systemlist=sorted(systemlist)
                remaining.remove(i)
                board[i]=y
                print("system seleted pos:",i)
                break
    else:
        for i in sides1:
            if i in remaining:
                systemlist.append(i)
                sides1.remove(i)
                systemlist=sorted(systemlist)
                remaining.remove(i)
                board[i]=y
                print("system selected pos: ",i)
                break
        
'''function to check whether system has a chance to win'''
def is_system_wins():
    '''global winset
    global winsubset
    global sumofwinsetlists
    global placetomark'''
    for i in itertools.combinations(systemlist,2):
        if i in winsubset:
            indexofi=winsubset.index(i)
            placetomark=sumofwinsetlists[indexofi]-sum(i)
            if placetomark in remaining:
                return placetomark
            else:
                continue
        else:
            return False
'''function to check whether system loses'''
def is_system_lose():
    global winset
    global winsubset
    global sumofwinsetlists
    global placetomark1
    global lst
    global found
    for i in itertools.combinations(userlist,2):
        if i in winsubset:
            indexofi=winsubset.index(i)
            placetomark1=sumofwinsetlists[indexofi]-sum(i)
            if placetomark1 in remaining:
                found=1
                return placetomark1
            else:
                pass
        else:
            found=0
    if found==0:
        return False
'''function to check whether center is available'''
def is_center_available():
    if center in remaining:
        return True
    else:
        return False

'''function to check whether corner is available'''
def is_corner_available():
    for i in corners:
        if i in remaining:
            return i
'''function to check whether game won by system'''
def isgamewin():
    for i in itertools.combinations(systemlist,3):
        j=list(i)
        if j in winset:
            return True
'''function to check whether game won by user'''
def isgamewinuser():
    for i in itertools.combinations(userlist,3):
        j=list(i)
        if j in winset:
            return True
start_game()
