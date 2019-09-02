from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def start():
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
    bot = webdriver.Firefox()
    bot.get('https://twitter.com/login')
    time.sleep(3)
    emailType = ActionChains(bot)
    passwordType = ActionChains(bot)
    emailType.send_keys(emailWritten)
    emailType.perform()
    passwordType.send_keys(Keys.TAB)
    passwordType.send_keys(passwordWritten)
    passwordType.send_keys(Keys.RETURN)
    passwordType.perform()
    time.sleep(3)


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
startButton = Button(checkBoxFrame, text="Start", command=start)

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