from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def start():
    emailWritten = emailInput.get()
    passwordWritten = passwordInput.get()
    topicWritten = topicInput.get()
    delayWritten = int(delayInput.get())
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
    bot.get('https://twitter.com/search?q='+topicWritten+'&src=typed_query&f=live')
    time.sleep(3)
    n = 0
    while True:
        navigate = ActionChains(bot)
        like = ActionChains(bot)
        retweet = ActionChains(bot)
        navigate.send_keys('j')
        navigate.perform()
        time.sleep(1)
        if retweetWritten == 1:
            retweet.send_keys('t')
            retweet.send_keys(Keys.RETURN)
            retweet.perform()
                      
        if likeWritten == 1:
            like.send_keys('l')
            like.perform()
                    
        if retweetWritten == 1 and likeWritten == 1:
            n = n + 1
            print (n, ' likes and retweets completed')

        if retweetWritten == 1 and likeWritten == 0:
            n = n + 1
            print (n, ' retweets completed')

        if retweetWritten == 0 and likeWritten == 1:
            n = n + 1
            print (n, ' likes completed')

        time.sleep(delayWritten)


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
delayVariable = IntVar()

emailLabel = Label(labelFrame, text="Email/Username")
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