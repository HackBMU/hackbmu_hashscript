import os
import sys
import praw

from config import *
from image_resolver import *
from task_downloader import *

if __name__ == '__main__':
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         password=PASSWORD,
                         user_agent=USER_AGENT,
                         username=USERNAME)

    last_id = ''
    download_data = []

    # Checkpoint
    if os.path.isfile('checkpoint.txt'):
        with open('checkpoint.txt', 'r') as file:
            last_id = file.read()
            print("Loaded Checkpoint,", last_id)