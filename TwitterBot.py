from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time


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
        # email = bot.find_element_by_class_name('email-input')
        # password = bot.find_element_by_name('session[password]')
        # email.clear()
        # password.clear()
        # email.send_keys(self.username)
        # password.send_keys(self.password)
        # password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like_tweet(self,topic):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+topic+'&src=typed_query&f=live')
        time.sleep(3)
        n = 1
        while True:
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
                # time.sleep(1)
                # like.send_keys('l')
                # like.perform()
            


            if likeTweet == 'YES':
                like.send_keys('l')
                like.perform()
                    
            if retweetTweet == 'YES' and likeTweet == 'YES':
                print (n, ' likes + retweets completed')
                n = n + 1

            if retweetTweet == 'YES' and likeTweet == 'NO':
                print (n, ' retweets completed')
                n = n + 1

            if retweetTweet == 'NO' and likeTweet == 'YES':
                print (n, ' likes completed')
                n = n + 1
                
            time.sleep(delay)
                    # elif likeTweet == True and retweetTweet == False:
                #     like.send_keys('l')
                #     like.perform()
                #     time.sleep(1)
                #     print (n, ' likes completed')
                #     n = n + 1
                #     time.sleep(delay)
                #     elif likeTweet == False and retweetTweet == True:
                #         retweet.send_keys('t')
                #         retweet.send_keys(Keys.RETURN)
                #         retweet.perform()
                #         print (n, ' retweets completed')
                #         n = n + 1
                #         time.sleep(delay)
            

            
email = input("Enter your email \n")
password = input("Enter your password \n")
topic = input("Enter your topic \n")
retweetTweet = ( input("Do you want to auto-retweet ? \n Type YES or NO \n"))
likeTweet = ( input("Do you want to auto-like ? \n Type YES or NO \n"))
delay = int ( input("Enter your delay time. 10 is recommended\n") )
ed = TwitterBot(email,password)
ed.login()
ed.like_tweet(topic)

