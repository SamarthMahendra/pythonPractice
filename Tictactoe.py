import time
import emoji
import random
board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def inputhuman():
    #inputting co-ordinates from the user
    print("Enter Co-ordinates :")
    i=int(input("Enter i : "))
    j=int(input("enter j : "))
    if board[i][j] == " " and i<3 and j<3:
        board[i][j]="x"
    else :
        print("Invalid move")
        print("Enter again ")
        inputhuman()
'''def chooseletter():
    playerletter = input("input player letter : ")
    return playerletter'''
def display():
    for rows in board:
        print(rows)
def minimax(board,depth,ismaximizing):
    result = checkwinner(board)
    if result =="x" :
        score= -1

        return score
    elif result =="o" :
        score= +1

        return score
    elif result == "draw":
        score= 0

        return score

    if ismaximizing :
        bestscore = 2
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j]="x"
                    score = minimax(board, depth+1, False)
                    board[i][j] = " "
                    bestscore = min(bestscore, score)
        return bestscore
    else:
        bestscore = -2
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j]="o"
                    score = minimax(board, depth+1, True)
                    board[i][j] = " "
                    bestscore = max(bestscore, score)
        return bestscore



def computerplay():
    '''

     played = 0
    if playerletter=="x" :
       for i in range(3):

           for j in range(3):
               if board[i][j] == " ":
                   board[i][j] = "o"
                   played = 1
                   break
           if played ==1:
               break

    else:
       for i in range(3):
           for j in range(3):
               if board[i][j] == " ":
                   board[i][j] = "x"
                   played =1
                   break
           if played ==1:
               break

    n++
    '''
    bestscore = -100
    for i in range(3):
        for j in range(3):
            if board[i][j] == " " :
                board[i][j]= "o"
                score = minimax(board,0,True)
                board[i][j]=" "
                if(score > bestscore):
                    bestscore=score
                    bestmove = [i,j]
    print(str(bestmove[0])+","+ str(bestmove[1])+" is the best move based on all possiblities using minmax algorithm ")
    board[bestmove[0]][bestmove[1]]="0"


def checkwinner(board):
    #rows check

    for rows in range(3):

            if board[rows][0] == board[rows][1] and board[rows][0] == board[rows][2] and board[rows][0] != " " :
                return board[rows][0]
    #cols check
    for cols in range(3):

        if board[0][cols] == board[1][cols] and board[0][cols] == board[2][cols] and board[0][cols] != " ":
            return board[0][cols]
    #dialognal check
    if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0] != " " :
        return board[0][0]
    if board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2] != " " :
        return  board[1][1]
    else :
        c=0
        for i in range(3):
            for j in range(3):
                if board[i][j] != " ":
                    c=c+1
        if c == 9 :
            return  "draw"
        return ""


def play():

    n=0
    print("-----Welcome to TicTacToe------")
    print("Tossing a Coin ..... ")
    for i in range(3):
        time.sleep(1)
    c=random.choice([0, 1])
    if c==0:
        print("Computer won the toss")
    else:
        print(" You have won the toss")

    while n < 10:

        if c==0:
            display()
            result = checkwinner(board)
            if result != "" and result != "draw":
                print(checkwinner(board) + " is winneer")
            elif result == "draw":
                print("Draw")

            print("......Computer Playing......")
            for i in range(3):
                time.sleep(1)
            computerplay()
            n=n+1
            display()
            result = checkwinner(board)


            if result != "" and result != "draw":
                print(result + " is winneer")
                break
            elif result == "draw":
                print("--------Draw  : "+emoji.emojize(":zipper-mouth_face:")+"--------")
                break
            inputhuman()
            n=n+1

        else:
            display()
            result = checkwinner(board)
            if result != "" and result != "draw":
                print(checkwinner(board) + " is winneer")
                break
            elif result == "draw":
                print("Draw")
                break
            inputhuman()
            n = n + 1
            display()
            if result != "" and result != "draw":
                print(result + " is winneer")
                break
            elif result == "draw":
                print("--------Draw  : " + emoji.emojize(":zipper-mouth_face:") + "--------")
                break
            print("......Computer Playing......")
            for i in range(3):
                time.sleep(1)
            computerplay()
            n = n + 1

'''
define a function where in if computer plays first use a custom funtion where in it plays double win method

'''


play()
