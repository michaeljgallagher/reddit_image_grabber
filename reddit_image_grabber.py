import praw
import requests
import os

reddit = praw.Reddit()

print('Checking to see if "bike_pics" directory exists...')
if os.path.exists('bike_pics'):
    print('Directory already exists, proceeding...')
else:
    print('Directory does not exist\nCreating directory "bike_pics"')
    os.makedirs('bike_pics')

os.chdir('bike_pics')

for submission in reddit.subreddit('Bikeporn').top(time_filter='day', limit=10):
    if submission.url[-4:] in ['.jpg', '.png']:
        print('Found image from submission: {}'.format(submission.title))
        file_name = submission.url.split('/')[-1]
        if file_name not in os.listdir():
            r = requests.get(submission.url)
            print('Saving file as: {} to {}'.format(file_name, os.getcwd()))
            with open(file_name, 'wb') as f:
                f.write(r.content)
                f.close()
        else:
            print('{} already found in {}'.format(file_name, os.getcwd()))

os.chdir('..')
