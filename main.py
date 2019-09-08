import praw
import os
import requests
import configparser

# Connect to settings.ini
pathname = os.path.dirname(os.path.realpath(__file__))
iniFile = os.path.abspath(pathname) + '/settings.ini'
config = configparser.ConfigParser()
config.read(iniFile)

reddit = praw.Reddit(client_id=config['RAPI']['client_id'],
    client_secret=config['RAPI']['client_secret'], 
    password=config['RAPI']['password'],
    user_agent=config['RAPI']['user_agent'], 
    username=config['RAPI']['username'])

subreddit = reddit.subreddit('funny')

hot_python = subreddit.hot()

hot_python = subreddit.hot(limit=100)
for submission in hot_python:
    if not submission.stickied:
        #print(dir(submission))
#         print('Title: {}, ups: {}, downs: {}, Have we visited?: {}, image: {}'.format(submission.title,
#        submission.ups,
#        submission.downs,
#        submission.visited,
#        submission.url,
#        ))
        print('image: {}'.format(submission.url))

        url = submission.url
        page = requests.get(url)
        f_ext = os.path.splitext(url)[-1]
        if (f_ext.endswith('.jpg') or f_ext.endswith('.png') or f_ext.endswith('.gif')):
            f_name1 = url.split('/')[-1].split('.')[0]
            f_name_full = '{}{}'.format(f_name1, f_ext)
            with open(f_name_full, 'wb') as f:
                f.write(page.content)
#        print(f_name_full)