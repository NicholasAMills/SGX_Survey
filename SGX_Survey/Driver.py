from tkinter import *
import tkinter.messagebox
import tkinter as tkr
import pandas as pd
import csv

def saveData(rData, cData, lData, dData, eData, oData):
    with open("survey.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerow(["Gameplay Rating", "Controls", "Likes", "Dislikes", "Puzzle Ideas", "Other"])
        writer.writerow([rData, cData, lData, dData, eData, oData])

def testData(input):
    global gameRating, controlsRating, likes, dislikes, environment, other_opinions
    ratingData = gameRating.get()
    controlsData = controlsRating.get()
    likesData = likes.get(0.0, END)
    dislikesData = dislikes.get(0.0, END)
    environmentData = environment.get(0.0, END)
    otherData = other_opinions.get(0.0, END)
    print(ratingData)
    print(controlsData)
    print(likesData)
    print(dislikesData)
    print(environmentData)
    print(otherData)
    tkinter.messagebox.showinfo("Thank you!", "Thanks for playing our game! :)")
    saveData(ratingData, controlsData, likesData, dislikesData, environmentData, otherData)
    clearData()

def clearData():#a, b, c, d, e, f, g):
    global gameRating, controlsRating, likes, dislikes, environment, other_opinions
    gameRating.set(10)
    controlsRating.set("Easy to understandand and use")
    likes.delete(0.0, END)
    dislikes.delete(0.0, END)
    environment.delete(0.0, END)
    other_opinions.delete(0.0, END)


root = Tk()  # create blank window
root.geometry("600x250")
root.title("Nekiri's Tail Survey")
root.geometry("1000x500")

# Labels
topLabel = Label(root, text="\tHow would you rate the following categories?", font=24)  # create a label
gameplayLabel = Label(root, text="Please rate the gameplay from 1-10")
controlsLabel = Label(root, text="Controls:")
likesLabel = Label(root, text="Tell us something things you liked:")
dislikesLabel = Label(root, text="Tell us something you didn't like:")
puzzleLabel = Label(root, text="What kind of puzzles would you like to see?")
otherOpinionLabel = Label(root, text="Any other comments?")

# Place labels
topLabel.grid(row=0)
gameplayLabel.grid(row=1)
controlsLabel.grid(row=3)
likesLabel.grid(row=4)
dislikesLabel.grid(row=6)
puzzleLabel.grid(row=8)
otherOpinionLabel.grid(row=10)

# Get input
# likes = Entry(root)  # input for likes
# dislikes = Entry(root)  # input for dislikes
# environment = Entry(root)  # input for environment/puzzle suggestions
# other_opinions = Entry(root)  # input for other opinions

likes = Text(root, width=50, height=4, wrap=WORD)
dislikes = Text(root, width=50, height=4, wrap=WORD)
environment = Text(root, width=50, height=4, wrap=WORD)
other_opinions = Text(root, width=50, height=4, wrap=WORD)

# Place input
#gameplayRating.grid(row=1, column=1)
likes.grid(row=4, column=1)
dislikes.grid(row=6, column=1)
environment.grid(row=8, column=1)
other_opinions.grid(row=10, column=1)

# Game Rating Menu
gameRating = IntVar(root)
gameRating.set(10)
gameRatingMenu = OptionMenu(root, gameRating, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10).grid(row=1, column=1)

# Controls Menu
controlsRating = StringVar(root)
controlsRating.set("Easy to understand and use")
controlsMenu = tkr.OptionMenu(root, controlsRating, "Easy to understand and use", "Confusing in some parts", "Not clear, need work").grid(row=3, column=1)

# Button
submitButton = Button(root, text="Submit")
submitButton.bind("<Button-1>", testData)
submitButton.grid(row=20, column=1)

root.mainloop()  # display to screen
