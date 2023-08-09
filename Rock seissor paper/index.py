import random

name = input("Enter your name : ")


def game(name):
    choose = input("Enter anyone {ROCK, SCISSOR , PAPER} : ")

    choose = choose.upper()
    list = ["ROCK" , "SCISSOR" , "PAPER"]
    randomChoose = random.choice(list)
    ans=("COMPUTER CHOOSE : " ,randomChoose)
    
    if(choose=="ROCK" and randomChoose=="ROCK"):
        ans=("TRY AGAIN!")
        return ans
    elif(choose=="ROCK" and randomChoose=="SCISSOR"):
        ans=(name,"IS WINNER!")
        return ans
    elif(choose=="ROCK" and randomChoose=="PAPER"):
        ans=("COMPUTER IS WINNER!")
        return ans
    elif(choose=="SCISSOR" and randomChoose=="ROCK"):
        ans=("COMPUTER IS WINNER!")
        return ans
    elif(choose=="SCISSOR" and randomChoose=="SCISSOR"):
        ans=("TRY AGAIN!")
        return ans
    elif(choose=="SCISSOR" and randomChoose=="PAPER"):
        ans=(name,"IS WINNER!")
        return ans
    elif(choose=="PAPER" and randomChoose=="ROCK"):
        ans=(name,"IS WINNER!")
        return ans
    elif(choose=="PAPER" and randomChoose=="SCISSOR"):
        ans=("COMPUTER IS WINNER")
        return ans
    elif(choose=="PAPER" and randomChoose=="PAPER"):
        ans=("TRY AGAIN!")
        return ans

answer = game(name)
print(answer)



