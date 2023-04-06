from tkinter import *
import random

number = 0

window = Tk()
window.title("number guesing game 4!!1!!1")
window.geometry("530x500")

def exit():
    "dummy function"
    pass


window.protocol("WM_DELETE_WINDOW", exit)


def leave():
    #window.quit()
    wrongmove2 = Tk()
    wrongmove2.title("bad choice.")
    wrongmove2.configure(bg="red")
    wrongmove2.geometry("620x500")
    title2 = Label(wrongmove2, bg="red",text="T̷̜̝̮͑h̷̨̥͕͍̱͉̲̃̎̑̚e̷̲̓́͗͑͗͒̉r̵͎̪̣͈̆̔e̶͉̦͗̂̅͋̑ͅ ̶̺̘̪͉̘̳̼̪̃ȉ̶̞̺͉͔̄̽͊̅͋͘͝ͅs̴̖̲͉̈́̅͗͗ ̴͖͈̘͙̲̮̟͆ń̶͕̰̞͇̻͐o̷̪̽̈̀̚͝ ̸͚̫̳̬̜̭͔͉̐̃̓̒̚ê̴̹̑̆̅s̴͍̟̻̪̋͊̐c̶̩̰̳̍̐́͑̚ã̴̡̼̱̓͑ͅp̸͎̥̿̎̈́̇̂̔͠e̸̗̤̍͒͗.̸̢̺̣̼̲̾̓͒̇͊̑̈͝ͅ", font=("Comic Sans MS", 45))
    title2.place(x=20, y=160)
def generate():
    global randomize
    global number
    difficult = (difficulty.get())
    if difficult == "easy" or difficult == "medium":
        wrongmove=Tk()
        wrongmove.title("bad choice.")
        wrongmove.configure(bg="red")
        wrongmove.geometry("620x500")
        title = Label(wrongmove, bg="red", text="H̴͎̿͌̑̌̿a̵̩̞̅̆̀̀́r̶͎͇̳̃͐̆͒̍d̴͓̈́̐͜ ̷̩̹̇͝M̶͉̦̫̹̓̏̿́͝o̷̱̼͓̰̪̐̂̕d̶͓̥̅̔ȩ̷́̈́́̐͝ ̴̗̼͚̘̼͋̓̕Ş̶̢̜̗͗ę̶͎̞̫̌̀͘l̵̨̮͉̣͇̀̏̌e̷̡̩̩͕͐̊̈́͂͆ç̷̙̲̥̩͂̈́̈́͒͒͂̑̎̇̊̚t̷͍͊̑́e̷̛͇̒̂̌d̷̗͊̑́̎̕.̴̼̫͇̎\nÝ̵̙̾̔ŏ̷͍̘̱̚u̸̺̿ ̵̯̻̾̏m̸̩͉̐a̶̜̔y̶͉̹̅ ̷̩̈́̌̈n̸͕͙͚̆̐̒o̷̧̜͊w̴͓͠ ̵͎̖̓ć̵̝̻l̴̙̓̄̇ȍ̴͈̏s̵̪̖̻͗̚ḙ̵̌̄ ̸̛̮̪͆̐t̵̩̮͑ḧ̸͚̖̭́i̸̪̣͂̒s̴͚̹̀ ̴̢̮̐͗͜ẘ̴̖̹̣͆͛ȋ̴̡n̷̘̯̈́ḋ̶̘̹̮o̴̝͑̈́ẘ̴̹͇͙̈͘.̸͖̃̕", font=("Comic Sans MS", 30))
        title.place(x=20, y=150)
        number = random.randint(1, 963460186237187848)
    else:
        number = random.randint(1, 963460186237187848)

    randomize.place_forget()

def Game(event):
    guess = int(box.get())
    global number
    global randomize
    box.delete(0, END)

    if guess > number:
        display.configure(image=pointdown)

    elif guess < number:
        display.configure(image=pointup)

    elif guess == number:
        display.configure(image=correct)
        randomize.place(x=51, y=352)

pointup=PhotoImage(file="../../TkinterProjects/image (4).png")
pointdown=PhotoImage(file="../../TkinterProjects/image (3).png")
correct=PhotoImage(file="../../TkinterProjects/image.png")
dice=PhotoImage(file="../../TkinterProjects/game-die.png")

title = Label(window, text="gues the number 4!!!!!!!!!", font=("Comic Sans MS", 30))
title.place(x=0, y=0)

difficulty = StringVar()

easy = Radiobutton(window, text="easy mode!!!!", variable=difficulty, font=("Comic Sans MS", 9), relief='groove',
                   value="easy")
easy.place(x=0, y=60)

medium = Radiobutton(window, text="medium mode 😡😡😡😡😡", variable=difficulty, font=("Comic Sans MS", 9),
                     relief='groove', value="medium")
medium.place(x=95, y=60)

hard = Radiobutton(window,
                   text="̨̗͕̭̻̦͉̠̓́͆͆̑̚̚ ̷̛͙̼̮̪̇̆̔͘ḫ̷̙͎̈́̅̅ḁ̴̢͈͉̻̹͉̋͛̄̑̊̓͒̈́̽͆̽̅̊r̴̡̻͈͌͒͆̋͌͆̍̀̈́͋̏̕ͅd̷̜͇̬̮̯̪̽̽͝ ̸͎̯͕̪͚̬̩̠͇̅̔̿̾̆̒̀̓̋̏͑̿ͅm̵̗͋̓̋̆̎̆͐͊͘͠ō̷̧͕̳̤͎̳̮̬̳̉̒̇̆̀̄̓̕͘͠ͅd̶̼̝̪̳͍͈̤̺̝͓͖͍̲̀̀̀͋ë̶̞̗̦̝͇̘͖̣͕̠͙͎́̐̀͑̂̈́̅̓͝͠͠ͅ ̵̴̨͙͎͎͖̌̌̔̌̋̅͌̑̈́̉  🤬🤬💀🤬 ┗|｀O′|┛",
                   variable=difficulty, font=("Comic Sans MS", 9), relief='groove', value="hard")
hard.place(x=280, y=60)

description = Label(window,
                    text="the code will pick a random number.\n easy mode is 1-100, medium is 1-250,\n and hard mode is 1-963460186237187848!🥰!!! good luck 🔫😉🔪",
                    font=("Comic Sans MS", 10))
description.place(x=0, y=100)

box = Entry(window, font=("Comic Sans MS", 23), relief='groove')
box.place(x=51, y=352)

display = Label(window, text="select a \n mode 😃", font=("Comic Sans MS", 35), relief='groove')
display.place(x=120, y=180)

exit = Button(window,
              text="leave the é̸̠̜̦̺̘͓̜̤̱͈̿́̉͊̑́́̈͝t̵̨͎̲͎͔̬̅̓ḝ̶̧͈̯̼̤̮̻̼̼̎̏̒̒̀̄̈́̾̕͜͝͠r̴̭͒̐͌̅̆̀̚ņ̴̋̃̈̽͌̆̕͝a̵̧̢̬̖̰̲̰̟̣͙̋̌̄̂̇͜͝l̶͙̟̝͇̠̋͂̈́̃̈̉́ ̶̧̡̖̞̪̫̞̹̗̺̖̍͐͛̓̎͐́̇̽̊̋͜͝p̵̧̗͍̻̺͋͂͂̐͜͝ͅr̵̦̭̯͌͌̔̀̕ḯ̴̡̢̢̯̞͔͈͉͈̎͌͋̍͑̚s̵̡̛͖͙̦̮̥̰̘͗͆͒͌̄̄͂́̆̆ờ̷̧̼̹̥̖̹͚̥̭̏͗͐̈̔̈́̇̾͜n̶̛͕̲̒́͗̿̅́́̚? 🥺 ",
              font=("Comic Sans MS", 20), relief='groove', command=leave)
exit.place(x=50, y=400)

randomize = Button(window, text="̲ s̷̳͖̗̰͉̠̰̝̈́̎̑̅͑͠ͅe̶̢͓͎̤̫̦͈̞͒͗̇̎̀̏̈́̍̄̕͠͝ǎ̷̢̢̮͔̫̼̼l̴̮̥͇̈́̆̀͂̓͐ ̶̧̡̢̭̘̀̋̿́̋y̶̙̱̰̻̥͛͌͛̈́͝o̴̧̨̤͓̘͈̮̥̣̭͖̹̒́̇̅̈́̏̏̂̚͠͝ͅû̴͎̘̩̀́͌̂̇͛̌̓͘͝͝r̴̢̛͖͈͙̥͎̱̤̼̯̗̟͊̅̓̃̎̃͗͒́́ ̶̳͓̤̻̠̞̝͛͐̒̆̀̌̏͐́̽̐͜͠f̷̡̢̹̫̘̰̤̳̤͇̟͂͆ȧ̶̛̠͖̟̭͓͙̫̹̞͍͒̇͛̈́̊͘͝t̴͖͎̳͇̝͉̟̣̰̀̆̀͝ȇ̵̛͍̹͉̀̄̽͐͠  (randomize the number)", font=("Comic Sans MS", 15), relief='groove', command=generate)
randomize.place(x=51, y=352)

window.bind("<Return>", Game)

window.mainloop()