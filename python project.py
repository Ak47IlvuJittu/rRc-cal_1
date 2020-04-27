import random
from tkinter import *
import tkinter.messagebox

def random_number():

    ch = 'y'
    while(ch=='y')or(ch=='Y'):
        number = random.randint(1,999)
        trial = 1
        name = input("Hello\nWelcome to the game *RANDOM NUMBER*\nEnter your name\n")
        print("hello", name+".",)
        a = input("would you like to play a game?[y or n]\n")
        if a == "n":
            print("okay:(")
            quit()



        if a == "y":
            print("I've chosen a number between 1 to 999\n")
            guess = int(input("guess a number between 1 to 999\n"))
            if guess>number:
                print("number is lesser than",guess)
            if guess<number:
                print("number is greater than",guess)

        while guess != number:
            trial+=1
            guess = int(input("try again:"))
            if guess<number:
                print("number is greater than",guess)
            if guess>number:
                print("number is lesser than",guess)
        if guess == number:
            print("Wowwww!!you are right!!you win!!\n")
            print("number of trials=",trial)

        print("do you want to play(y or n):",end="")
        ch=input()

def hangman():
    print("hello,welcome to hangman\n")
    answerlist = ['hello','world','percent','city','bread','harry potter','python']
    dict={'hello':'common greeting','world':"planet earth",'percent':"fraction of 100",'city':"human settlement",'bread':"eatable",'harry potter':"great young wizard",'python':"popular programming language"}
    random.shuffle(answerlist)
    answer = list(answerlist[0])
    display = []
    used=[]
    display.extend(answer)
    used.extend(display)
    for i in range(len(display)):
        display[i]='_'
    
    print(' '.join(display))
    print()
    count=0
    sum=0
    a=0
    print("clue:",dict[answerlist[0]],"\n")
    while count<len(answer):

        guess = input("please guess a letter\n")

        guess=guess.lower()
        sum = sum+1
        print('trial:',sum)

        for i in range(len(answer)):
            if answer[i]==guess and guess in used:

                display[i]=guess
                count=count+1
                used.remove(guess)
        if guess not in display:
            a=a+1
            print("OOPS!!\nsorry,wrong guess:(")
        if a==4:
            print("You lost:(\n")
            break

        print("you have guessed:",count,"correct letters.")
        print(" ".join(display))
        print()
        if count==len(answer):
            print("well done you guessed the word in",sum,'trials.congratulations!!:)')
def tictac():
    tk = Tk()
    tk.title("tic tac toe")

    global click
    click = True

    def checker(buttons):
        global click
        if buttons["text"]==" " and click==True:
            buttons["text"]="x"
            click=False
        elif buttons["text"]==" " and click==False:
            buttons["text"]="o"
            click = True

        if (button1["text"]=="x" and button2["text"]=="x" and button3["text"]=="x" or
            button4["text"]=="x" and button5["text"]=="x" and button6["text"]=="x" or
            button7["text"]=="x" and button8["text"]=="x" and button9["text"]=="x" or
            button3["text"]=="x" and button5["text"]=="x" and button7["text"]=="x" or
            button1["text"]=="x" and button5["text"]=="x" and button9["text"]=="x" or
            button1["text"]=="x" and button4["text"]=="x" and button7["text"]=="x" or
            button2["text"]=="x" and button5["text"]=="x" and button8["text"]=="x" or
            button3["text"]=="x" and button6["text"]=="x" and button9["text"]=="x"):
            tkinter.messagebox.showinfo("winner x","you have just won a game")

        elif (button1["text"]=="o" and button2["text"]=="o" and button3["text"]=="o" or
              button4["text"]=="o" and button5["text"]=="o" and button6["text"]=="o" or
              button7["text"]=="o" and button8["text"]=="o" and button9["text"]=="o" or
              button3["text"]=="o" and button5["text"]=="o" and button7["text"]=="o" or
              button1["text"]=="o" and button5["text"]=="o" and button9["text"]=="o" or
              button1["text"]=="o" and button4["text"]=="o" and button7["text"]=="o" or
              button2["text"]=="o" and button5["text"]=="o" and button8["text"]=="o" or
              button3["text"]=="o" and button6["text"]=="o" and button9["text"]=="o" ):
              tkinter.messagebox.showinfo("winner o","you have just won a game")


        if button1["text"]!=" " and button2["text"]!=" " and button3["text"]!=" " and button4["text"]!=" " and button5["text"]!=" " and button6["text"]!=" " and button7["text"]!=" " and button8["text"]!=" " and button9["text"]!=" ":

            tkinter.messagebox.showinfo("draw","match drawn")






    buttons=StringVar()
    button1 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button1))
    button1.grid(row=1,column=0)
    button2 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button2))
    button2.grid(row=1,column=1)
    button3 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button3))
    button3.grid(row=1,column=2)
    button4 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button4))
    button4.grid(row=2,column=0)
    button5 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button5))
    button5.grid(row=2,column=1)
    button6 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button6))
    button6.grid(row=2,column=2)
    button7 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button7))
    button7.grid(row=3,column=0)
    button8 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button8))
    button8.grid(row=3,column=1)
    button9 = Button(tk,text=" ",font=("Times 26 bold"),height = 4,width = 8,command=lambda:checker(button9))
    button9.grid(row=3,column=2)

    tk.mainloop()










def main():
    ch='y'
    while(ch=='y' or ch=='Y'):
        print('***********WELCOME TO THE GAMES WORLD***********')
        print('1.~guessing a random number~')
        print('2.~hangman~')
        print("3.tic_tac_toe")
        print('4.~quit~')
        print('enter your choice\npress 1 to play random number\npress 2 to play hangman\npress 3 to play tic tac toe\npress 4 to exit')
        option=int(input())
        if option==1:
            random_number()
        elif option==2:
            hangman()
        elif option==3:
            tictac()

        elif option==4:

            quit()

        print("do you want to continue playing(y or n)?",end="")
        ch=input()

main()
