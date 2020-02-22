# reddit Image Grabber

Python script that utilizes [PRAW](https://praw.readthedocs.io/en/latest/index.html) to download pictures from posts containing images from your favorite subreddit (currently pointed at [/r/Bikeporn](https://reddit.com/r/Bikeporn)).

You must update `praw.ini` with your `client_id`, `client_secret`, `username`, and `password` in order to use the script.

Currently saves the top 10 images from the past day for that subreddit into a directory. Will make this more customizable in the future...
