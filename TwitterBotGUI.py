from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_email():
    emailWritten = emailInput.get()
    passwordWritten = passwordInput.get()
    topicWritten = topicInput.get()
    delayWritten = delayInput.get()
    retweetWritten = retweetCheck.get()
    likeWritten = likeCheck.get()
    print(emailWritten)
    print(passwordWritten)
    print(topicWritten)
    print(delayWritten)
    print(retweetWritten)
    print(likeWritten)
    bot = 

root = Tk()
labelFrame = Frame(root)
inputFrame = Frame(root)
checkBoxFrame = Frame(root)
checkBoxLabelFrame = Frame(root)
labelFrame.pack(side=LEFT, padx=20)
inputFrame.pack(side=LEFT, padx=20)
checkBoxFrame.pack(side=TOP)
checkBoxLabelFrame.pack(side=LEFT)
retweetCheck = IntVar()
likeCheck = IntVar()

emailLabel = Label(labelFrame, text="Email")
passwordLabel = Label(labelFrame, text="Password")
topicLabel = Label(labelFrame, text="Topic")
delayLabel = Label(labelFrame, text="Delay")

emailInput = Entry(inputFrame)
passwordInput = Entry(inputFrame, show="*",)
topicInput = Entry(inputFrame)
delayInput = Entry(inputFrame)


retweetLabel = Checkbutton(checkBoxFrame, text="Auto Retweet", variable=retweetCheck)
likeLabel = Checkbutton(checkBoxFrame, text="Auto Like", variable=likeCheck)
startButton = Button(checkBoxFrame, text="Start", command=test_email)

emailLabel.pack()
passwordLabel.pack()
topicLabel.pack()
delayLabel.pack()
emailInput.pack()
passwordInput.pack()
topicInput.pack()
delayInput.pack()
retweetLabel.pack()
likeLabel.pack()
startButton.pack()

root.resizable(False, False)
root.mainloop()