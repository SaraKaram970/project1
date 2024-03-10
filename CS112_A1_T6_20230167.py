#description:
#........... aborard of 3x3 is display and player1 takes odd numbers (1,9)and player 2 takes even
#(2,8).odd number start ,useeach number only once. the frist player to complete a line that add up to 15 is the winner

# Author: sara karam said
#Id: 20230167
#ٍSection:----

#Version:1
#Date: 2/3/2024


# Welcome Message
print("Welcome Tic_Tac_Toe with numbers")

game_board = [["","",""],["","",""],["","",""]]
list1=[1,3,5,7,9]
list2=[0,2,4,6,8]

# display game_board
def print_game_board():
    print("      1   2   3")
    print("    +---+---+---+")
    for x in range(3):
        print(x + 1, "  |",end="")
        for y in range(3):
            if game_board[x][y]=="" :
                print("   |",end="")
            else:
                print("",game_board[x][y],"|",end="")
        print("\n    +---+---+---+")


# Modify _Game board
def modify_game_board(sp, number_picked):
    game_board [int(sp[0]) - 1] [int(sp[1]) - 1]=number_picked

# available _position in game board
def is_position_available(sp):
    if game_board[int(sp[0]) - 1][int(sp[1]) - 1]== "" :
        return True
    else:
        return False
    
# check winner
def check_win():
# Horizontal check 
    for x in range(3):
        if (game_board[x][0]!= "") and (game_board[x][1]!= "") and (game_board[x][2]!= "") :
            if game_board[x][0]+game_board[x][1]+game_board[x][2] ==15:
                return True
# Vertical check
    for y in range(3):
        if (game_board[0][y]!="") and  (game_board[1][y]!="") and  (game_board[2][y]!= ""):
            if game_board[0][y]+game_board[1][y]+game_board[2][y]==15:
                return True
#Diagonal L to R
    if (game_board[0][0]!= "") and (game_board[1][1]!= "") and (game_board[2][2] != ""):
        if game_board[0][0]+game_board[1][1]+game_board[2][2]==15:
            return True
#Diagonal R to L
    if (game_board[0][2]!= "") and (game_board[1][1]!= "") and (game_board[2][0]!= "") :
        if game_board[0][2]+game_board[1][1]+game_board[2][0]==15:
            return True
    return False

# check game draw
def is_game_draw():
    for i in range(3):
        for x in range(3):
            if game_board[i][x]=="":
                return False
    return True


j="y" 
counter=1
while j=="y"or j=="Y":
    if counter%2!=0: # turns' player1
        p ="player1"
        print(p,"turn")
    else:  # turns' player 2
        p ="player2" 
        print(p,"turn")
    while True:
        print_game_board() # display game_board
        choice=input("enter position: ")
        if choice not in ("11", "12", "13", "21", "22", "23", "31", "32", "33", ): # check position 
            print("invalid")
            continue
        elif is_position_available(choice) ==False: # check avaible position
            print("unavailable position")
            continue
        else:
            break
    while True:
        if counter%2!=0 :# player 1 turn
            print(list1) # display available numbers
            num = int(input("enter number odd from list1: "))
            if num not in (1,3,5,7,9): #check is num odd or not
                print("invalid number/n")
                continue
            else: 
                list1.remove(num) # check is odd number remove in list1
                break  
        else:
            print(list2)
            num = int(input("enter number even from list2: "))
            if num not in (0,2,4,6,8): # check is num even or not
                print("invalid number/n")
                continue
            else:
                list2.remove(num)# check is even number remove in list2
                break
    modify_game_board(choice,num)
    print_game_board()
    counter+=1
    if check_win()==True: # check winner player 1 or player 2
        print(p,"win")
        game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
        s=0
    elif is_game_draw(): # check Game draw or not
           print("Game draw")
           game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
           s=0
    else:
        s=1

    while s==0:
        j=input("Do you want to play again?(y/n)")
        if j not in ("y","Y","n","N",): # check if user want to continue game or not
            print("invalid")
            continue
        else:
            break