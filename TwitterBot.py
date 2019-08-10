from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains
from Xlib import XK, display, ext, X, protocol
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
            actions = ActionChains(bot)
            like = ActionChains(bot)
            like.send_keys('j')
            time.sleep(1)
            like.send_keys('l')
            like.perform()
            time.sleep(1)
            actions.send_keys('t')
            actions.send_keys(Keys.RETURN)
            actions.perform()
            print (n, ' likes + retweets completed')
            n = n + 1
            time.sleep(7)

            

ed = TwitterBot('putYourEmail@here.com','putYourPasswordHere') #configuring your login details
ed.login()
ed.like_tweet('putYourTopicHere') #rename the topic you want

