# TwitterBot
A simple bot for Twitter

# Disclaimer
Use it on your own risk.

# Features
For now, it's only
* Auto retweet
* Auto like

# Installation
You need this program to run ```TwitterBot```
* [python](https://www.python.org/downloads/)
* [gecko driver](https://github.com/mozilla/geckodriver/releases/tag/v0.24.0)
* [firefox](https://www.mozilla.org/en-US/firefox/)

And the step is :
* install ```python``` and ```firefox```
* copy ```gecko driver``` to python's directory. (Usually stored in ```C:\Users\[name_of_user]\AppData\Local\Programs\Python\[python_version])```
* edit ```TwitterBot``` in your favourite IDE
* scroll to bottom to configuring your login details and the topic.
```
ed = TwitterBot('putYourEmailInHere@example.com','putYourPasswordInHere') #configuring your login details
ed.login()
ed.like_tweet('putYourTopicToLikeAndRetweetInHere') #rename the topic you want
```
* save
* run the ```TwitterBot.py``` or execute
```python TwitterBot.py```

# Copyright
Bebas lah kalian curi, fork, clone atau download.
