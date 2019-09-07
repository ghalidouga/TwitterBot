from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import sys
import time
import getpass




class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = ActionChains(bot)
        password = ActionChains(bot)
        email.send_keys(self.username)
        email.perform()
        password.send_keys(Keys.TAB)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        password.perform()
        time.sleep(3)
    
    def like_tweet(self,topic):
        bot = self.bot
        urlBot = 'https://twitter.com/search?q='+topic+'&src=typed_query&f=live'
        bot.get(urlBot)
        
        time.sleep(3)
        n = 0
        x = 0
        while x < repeatAction:
            if bot.current_url != urlBot:
                resume = input("Paused. Do you want to Continue? \n Type YES to continue \n")
                while resume == 'YES':
                    bot.back()
                    time.sleep(3)
                    if bot.current_url == urlBot:
                        resume = 'NO'
            delayRandom = randint(delayRandomMin,delayRandomMax)
            navigate = ActionChains(bot)
            like = ActionChains(bot)
            retweet = ActionChains(bot)
            navigate.send_keys('j')
            navigate.perform()
            time.sleep(1)

            # Decide to like or retweet or both

            if retweetTweet == 'YES':
                retweet.send_keys('t')
                retweet.send_keys(Keys.RETURN)
                retweet.perform()
                      
            if likeTweet == 'YES':
                like.send_keys('l')
                like.perform()
                    
            if retweetTweet == 'YES' and likeTweet == 'YES':
                n = n + 1
                print (n, ' likes and retweets completed')

            if retweetTweet == 'YES' and likeTweet == 'NO':
                n = n + 1
                print (n, ' retweets completed')

            if retweetTweet == 'NO' and likeTweet == 'YES':
                n = n + 1
                print (n, ' likes completed')
                
            time.sleep(delayRandom)
            x = x + 1
            
        
        
    
        again = input("Finished! But do you want to do it again ? \n Type YES or NO \n")     
        if again == 'YES':
            ed.like_tweet(topic)
        if again == 'NO':
            sys.exit()     
            



print("TwitterBot v.1.3-alpha by ghalidouga")
email = input("Enter your email/username \n")
password = input("Enter your password \n")
topic = input("Enter your topic \n")
hashtagmode = input("Do you want to add a Hashtag(#) in your topic ? \n Type YES or NO \n")
retweetTweet = ( input("Do you want to auto-retweet ? \n Type YES or NO \n"))
likeTweet = ( input("Do you want to auto-like ? \n Type YES or NO \n"))
repeatAction = int(input("Enter how many times do you want to execute this bot. 100 is recommended \n"))
delayRandomMin = int(input("Enter your minimum random delay time. 8 is recommended \n"))
delayRandomMax = int(input("Enter your maximum random delay time. Must be higher than previous number \n"))
if hashtagmode == 'YES':
    topic = '%23'+topic
while delayRandomMin >= delayRandomMax:
    print("Your maximum delay time cannot be lower than minimum delay time")
    delayRandomMax = int(input("Enter your maximum random delay time. Must be higher than previous number \n"))


    

ed = TwitterBot(email,password)
ed.login()
ed.like_tweet(topic)



