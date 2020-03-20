from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from tkinter import *
import sys
import time
import getpass

def debugGui():
    print("test button")

root = Tk()
#LABEL GUI
titleLabel = Label(root, text="TwitterBot By ghaliDouga")
userEmailLoginLabel = Label(root, text="Username/Email")
passwordLabel = Label(root, text="Password")
topicLabel = Label(root,text="Topic")
hashtagLabel = Label(root, text="Hashtag")
retweetLabel = Label(root, text="Retweet")
likeLabel = Label(root, text="like")
howManyTimesLabel = Label(root, text="How Many Times")
delayMinLabel = Label(root, text="Delay Minimum")
delayMaxLabel = Label (root, text="Delay Maximum")
startButton = Button(root, text="Start Botting", padx=20, pady=10, command=debugGui)
#ENTRY GUI
userEmailLoginEntry = Entry(root, text="email")
passwordEntry = Entry(root, text="password")
topicEntry = Entry(root,text="topic")
hashtagEntry = Entry(root, text="hashtag")
retweetEntry = Entry(root, text="RT")
likeEntry = Entry(root, text="like")
howManyTimesEntry = Entry(root, text="howMany")
delayMinEntry = Entry(root, text="min")
delayMaxEntry = Entry(root, text="max")

#GUI POSITION
titleLabel.grid(row=0, column=1)
userEmailLoginLabel.grid(row=1, column=0)
passwordLabel.grid(row=2, column=0)
topicLabel.grid(row=3, column=0)
hashtagLabel.grid(row=4, column=0)
retweetLabel.grid(row=5, column=0)
likeLabel.grid(row=6, column=0)
howManyTimesLabel.grid(row=7, column=0)
delayMinLabel.grid(row=8, column=0)
delayMaxLabel.grid(row=9, column=0)
startButton.grid(row=10, column=1)

userEmailLoginEntry.grid(row=1, column=1)
passwordEntry.grid(row=2, column=1)
topicEntry.grid(row=3, column=1)
hashtagEntry.grid(row=4, column=1)
retweetEntry.grid(row=5, column=1)
likeEntry.grid(row=6, column=1)
howManyTimesEntry.grid(row=7, column=1)
delayMinEntry.grid(row=8, column=1)
delayMaxEntry.grid (row=9, column=1)



root.mainloop()



# class TwitterBot:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#         self.bot = webdriver.Firefox()

    

#     def login(self):
#         bot = self.bot
#         bot.get('https://twitter.com/login')
#         time.sleep(3)
#         email = ActionChains(bot)
#         password = ActionChains(bot)
#         email.send_keys(self.username)
#         email.perform()
#         password.send_keys(Keys.TAB)
#         password.send_keys(self.password)
#         password.send_keys(Keys.RETURN)
#         password.perform()
#         time.sleep(3)
    
#     def like_tweet(self,topic2):
#         bot = self.bot
#         urlBot = 'https://twitter.com/search?q='+topic2+'&src=typed_query&f=live'
#         bot.get(urlBot)
#         print(topic2) #debug
        
#         time.sleep(3)
#         n = 0
#         x = 0
#         while x < repeatAction:
#             if bot.current_url != urlBot:
#                 resume = input("Paused. Do you want to Continue? \n Type YES to continue \n")
#                 while resume == 'YES':
#                     print("Trying to continue... please dont click anything.")
#                     bot.back()
#                     time.sleep(3)
#                     if bot.current_url == urlBot:
#                         resume = 'NO'
#                         navigateResume = ActionChains(bot)
#                         navigateResume.send_keys('j')
#                         navigateResume.perform()
#                         print("Bot Continue to working.")

#             delayRandom = randint(delayRandomMin,delayRandomMax)
#             navigate = ActionChains(bot)
#             like = ActionChains(bot)
#             retweet = ActionChains(bot)
#             navigate.send_keys('j')
#             navigate.perform()
#             time.sleep(1)

#             # Decide to like or retweet or both

#             if retweetTweet == 'YES':
#                 retweet.send_keys('t')
#                 retweet.send_keys(Keys.RETURN)
#                 retweet.perform()
                      
#             if likeTweet == 'YES':
#                 like.send_keys('l')
#                 like.perform()
                    
#             if retweetTweet == 'YES' and likeTweet == 'YES':
#                 n = n + 1
#                 if n == 1:
#                     print (n, 'like and retweet completed')
#                 if n > 1:
#                     print (n, 'likes and retweets completed')

#             if retweetTweet == 'YES' and likeTweet == 'NO':
#                 n = n + 1
#                 if n == 1:
#                     print (n, 'retweet completed')
#                 if n > 1:
#                     print (n, 'retweets completed')

#             if retweetTweet == 'NO' and likeTweet == 'YES':
#                 n = n + 1
#                 if n == 1:
#                     print (n, 'like completed')
#                 if n > 1:
#                     print (n, 'likes completed')
                
#             time.sleep(delayRandom)
#             x = x + 1
            
        
        
    
#         again = input("Finished! But do you want to do it again ? \n Type YES or NO \n")     
#         if again == 'YES':
#             ed.like_tweet(topic2)
#         if again == 'NO':
#             sys.exit(0)     
            



# print("TwitterBot v.2.1-alpha by ghalidouga")
# email = input("Enter your email/username \n")
# password = input("Enter your password \n")
# topic2 = input("Enter your topic \n")
# spasi = topic2.find(' ')
# while (spasi != -1):
#     if (spasi != -1):
#         topic2 = list(topic2)
#         topic2[spasi] = '%20'
#     topic2 = ''.join(map(str, topic2))
#     spasi = topic2.find(' ')
# print(topic2) #debug
# print(spasi) #debug
# print(topic2) #debug
# hashtagmode = input("Do you want to add a Hashtag(#) in your topic ? \n Type YES or NO \n")
# retweetTweet = ( input("Do you want to auto-retweet ? \n Type YES or NO \n"))
# likeTweet = ( input("Do you want to auto-like ? \n Type YES or NO \n"))
# repeatAction = int(input("Enter how many times do you want to execute this bot. 100 is recommended \n"))
# delayRandomMin = int(input("Enter your minimum random delay time. 8 is recommended \n"))
# delayRandomMax = int(input("Enter your maximum random delay time. Must be higher than previous number \n"))
# if hashtagmode == 'YES':
#     topic2 = '%23'+topic2
# while delayRandomMin >= delayRandomMax:
#     print("Your maximum delay time cannot be lower than minimum delay time")
#     delayRandomMax = int(input("Enter your maximum random delay time. Must be higher than previous number \n"))


    

# ed = TwitterBot(email,password)
# ed.login()
# ed.like_tweet(topic2)



