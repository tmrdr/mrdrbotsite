
import markovify
import tweepy
import env
from random import randint
from time import sleep

with open ("botfood.txt") as botfood_file:
    botfood = botfood_file.read()

model = markovify.Text(botfood)

oldtext = []
back = []
backtext = []

class TwitterAPI:
    def __init__(self, botfood):
        self.load_botfood(botfood)

        consumer_key = env.consumer_key
        consumer_secret = env.consumer_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = env.access_token
        access_token_secret = env.access_token_secret
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



    def timeline(self):
        public_tweets = self.api.home_timeline()
        # print(public_tweets)
        for tweet in public_tweets:
                if tweet.user.screen_name != "tmrdrr":
                    if tweet.text not in oldtext:
                        if tweet.text not in backtext:
                            if "tmrdrr" in tweet.text.lower():
                                toReply = tweet.user.screen_name
                                self.tweet(toReply)
                                oldtext.insert(0, tweet.text)
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
        self.api.update_status("@" + toReply + " " + message)





    def automate(self, delay):
        while True:
            self.timeline()
            # self.search()
            sleep(delay)


def main():
    twitter = TwitterAPI("botfood.txt")
    twitter.backlog()
    twitter.automate(65)



if __name__ == "__main__":
    main()
