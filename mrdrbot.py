
import markovify
import tweepy
from env import keys
from random import randint
from time import sleep



oldtext = []
back = []
backtext = []

class TwitterAPI:
    def __init__(self, botfood):
        self.load_botfood(botfood)

        consumer_key = keys['consumer_key']
        consumer_secret = keys['consumer_secret']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = keys['access_token']
        access_token_secret = keys['access_token_secret']
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def load_botfood(self, botfood):
        with open (botfood) as botfood:
            botfood = botfood.read()
        self.model = markovify.Text(botfood)
        print(self.model)

    def backlog(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            if tweet.user.screen_name != "tmrdrr":
                backtext.insert(0, tweet.text)
                if tweet.user.screen_name not in back:
                    toReply = tweet.user.screen_name
                    self.tweet(toReply)
                    back.insert(0, tweet.user.screen_name)

    def follow(self):
        for follower in tweepy.Cursor(self.api.followers).items():
            follower.follow()
            print (follower.screen_name)



    def timeline(self):
        public_tweets = self.api.home_timeline()
        with open ("botfood.txt", "r") as botfood_file:
            botfood = botfood_file.read()
            model = markovify.Text(botfood)
        # print(public_tweets)
        with open ("botfood.txt", "a") as botfood_file:
            for tweet in public_tweets:
                    if tweet.user.screen_name != "tmrdrr":
                        if tweet.text not in oldtext:
                            if tweet.text not in backtext:
                                if "tmrdrr" in tweet.text.lower():
                                    toReply = tweet.user.screen_name
                                    self.tweet(toReply)
                                    oldtext.insert(0, tweet.text)
                                    tobeinserted = tweet.text
                                    tobeinserted = tobeinserted.split(' ', 1)[1]
                                    botfood_file.write(tobeinserted + "\n")

                                    # print(oldtext)
                                    if len(oldtext) > 15:
                                        oldtext.pop()

    # def search(self):
    #         message = self.model.make_short_sentence(120)
    #         for tweet in self.api.search(q="tmrdrr"):
    #             if "tmrdrr" in tweet.text.lower():
    #                     toReply = tweet.user.screen_name
    #                     self.tweet(toReply)





    def tweet(self, toReply):
        message = self.model.make_short_sentence(120)
        messageTwo = self.model.make_short_sentence(140)
        self.api.update_status("@" + toReply + " " + message)
        self.api.update_status(messageTwo)





    def automate(self, delay):
        while True:
            self.timeline()

            sleep(delay)


def main():
    twitter = TwitterAPI("botfood.txt")
    twitter.backlog()
    twitter.follow()
    twitter.automate(185)



if __name__ == "__main__":
    main()
