import tweepy

consumer_key = "yomamma"
consumer_secret = "yodadda"
access_token = "yodata"
access_token_secret = "yomon"


def main():
    auth = tweepy.OAuthHandler(
            consumer_key,
            consumer_secret)

    auth.set_access_token(
            access_token,
            access_token_secret)

    api = tweepy.API(auth)

    tweet = "Tweeting with #python"
    status = api.update_status(status=tweet) 

if __name__ == "__main__":
    main()
