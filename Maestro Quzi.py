from tkinter import *
from random import randint

qCount = 0
usedQuestions = []
actualAnswer = 0
usersAnswer = 0
points = 0

def readFile():

    data = []
    file = open("questions.txt",mode = "r")
    for line in file:
        data.append(line.strip().split(','))
    return data

def displayQuestion():

    data = readFile()
    global qCount, usedQuestions, actualAnswer

    randomQ = randint(0,len(data)-1)
    currentQuestion = str(data[randomQ][0])

    while currentQuestion in usedQuestions and len(usedQuestions)< len(data):
        randomQ = randint(0, len(data) - 1)
        currentQuestion = str(data[randomQ][0])

    if qCount < len(data):
        resetBtns()
        qNum.config(text="Question: {0}".format(qCount + 1))
        question.config(text = data[randomQ][1])
        btnA.config(text=data[randomQ][2])
        btnB.config(text=data[randomQ][3])
        btnC.config(text=data[randomQ][4])
        btnD.config(text=data[randomQ][5])

        qCount += 1
        usedQuestions.append(currentQuestion)
        actualAnswer = data[randomQ][6]

    else:
        gameOver.config(text ="GAME OVER \n\n Final score: %s"% points)
        gameOver.place(relwidth = 1,relheight = 1 )

def checkAnswer():
    global points
    if int (actualAnswer) == usersAnswer :
        points += 1
        score.config(text = "score: %s"% points)
    resetBtns()
    displayQuestion()


def btnPressed(Answer):

    resetBtns()

    if Answer == 1:
        btnA.config(fg = "#FFFFFF")
    elif Answer == 2:
        btnB.config(fg = "#FFFFFF")
    elif Answer == 3:
        btnC.config(fg = "#FFFFFF")
    elif Answer == 4:
        btnD.config(fg = "#FFFFFF")

    global usersAnswer
    usersAnswer = Answer

def resetBtns():

    btnA.config(fg="#000000")
    btnB.config(fg="#000000")
    btnC.config(fg="#000000")
    btnD.config(fg="#000000")

def Quiz():

    global qNum , question , btnA , btnB , btnC , btnD , gameOver , score , btnReset

    win = Tk()
    win.title("Masetro quiz")
    fgColour="#20212a"
    bgColour="#FEFCEE"
    text = ("PT Sans Caption", 24)
    win.geometry("1100x600")
    win.iconbitmap(r"quizIcon.ico")

    bgImage = PhotoImage(file = r"anime.png")
    Label(win , image = bgImage).place(relwidth = 1,relheight = 1)

    titleFrame=Frame(win, bg = bgColour )
    titleFrame.place(relwidth=1, relheight=0.08)

    Label(titleFrame,
          text="Masetro quiz",
          font = text,
          anchor=CENTER,
          fg=fgColour,
          bg=bgColour).place(relx=0, relheight=1)

    score = Label(titleFrame,
                  text ="score: 0",
                  font = text,
                  anchor = E,
                  fg = fgColour,
                  bg = bgColour)

    score.place(relx = 0.8,
                relwidth = 0.2,
                relheight = 1)


    qNum = Label(win,
                 fg = fgColour,
                 bg = bgColour,
                 font = text)

    qNum.place(relx = 0.1,
               rely = 0.15,
               relwidth = 0.8,
               relheight = 0.3)


    question = Label(win,
                     text = "PRESS TO START",
                     fg = fgColour,
                     bg = "#ECECEC",
                     font = text,)

    question.place(relx = 0.1,
                   rely = 0.25,
                   relwidth = 0.8,
                   relheight = 0.3)


    nxtImg = PhotoImage(file = r"Dha.png")


    nextBtn = Button(win,
                      text ="Next",
                      image = nxtImg,
                      bd = 0,
                      compound = CENTER,
                      command = checkAnswer)

    btnImg = PhotoImage(file=r"Dha.png")


    btnA = Button(win,
                  text="dhairya",
                  font=("Comic Sans MS", 20),
                  image = btnImg,
                  compound = CENTER,
                  command = lambda:btnPressed(1))

    btnA.place(relx = 0.1,
               rely = 0.6,
               relwidth = 0.35,
               relheight = 0.1)


    btnB = Button(win,
                  text="dhairya",
                  font=("Comic Sans MS", 20),
                  image = btnImg,
                  compound = CENTER,
                  command = lambda:btnPressed(2))

    btnB.place(relx = 0.55,
               rely = 0.6,
               relwidth = 0.35,
               relheight = 0.1)


    btnC = Button(win,
                  text="dhairya",
                  font=("Comic Sans MS", 20),
                  image = btnImg,
                  compound = CENTER,
                  command = lambda:btnPressed(3))

    btnC.place(relx = 0.1,
               rely = 0.8,
               relwidth = 0.35,
               relheight = 0.1)


    btnD = Button(win,
                  text="dhairya",
                  font=("Comic Sans MS", 20),
                  image = btnImg,
                  compound = CENTER,
                  command = lambda:btnPressed(4))

    btnD.place(relx = 0.55,
               rely = 0.8,
               relwidth = 0.35,
               relheight = 0.1)


    def hideStart():
        btnStart.destroy()
        displayQuestion()

        nextBtn.place(relx=0.91,
                      rely=0.35,
                      width=50,
                      height=50)

    btnStart = Button(win ,
                      text = "START",
                      font = ("Comic Sans MS", 20),
                      image = btnImg,
                      compound = CENTER,
                      command = hideStart)

    btnStart.place(relx = 0.1,
                   rely = 0.6,
                   relwidth = 0.8,
                   relheight = 0.3)

    gameOver = Label(win,
                     fg = "#FFFFFF",
                     bg = "#000000",
                     font = ("Comic Sans MS", 50))

    win.mainloop()

Quiz()
