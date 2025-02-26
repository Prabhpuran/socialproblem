from django.conf import settings
from mailjet_rest import Client
import tweepy

def send_mailjet_email(subject, html_content, to_email):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET))
    data = {
        'FromEmail': 'prabhpuran@gmail.com',
        'FromName': 'Hopeline',
        'Subject': subject,
        'Html-part': html_content,
        'Recipients': [{'Email': to_email}],
    }
    result = mailjet.send.create(data=data)
    return result

def post_tweet(content):
    auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        tweet = api.update_status(status=content)
        return tweet.id
    except AttributeError as e:
        print(f"Error posting tweet: {e}")
        return None
