from csv import *
from array import *
import praw
import time
import datetime
import calendar

reddit = praw.Reddit(
    client_id="nS1CZVpYoi_8bg",
    client_secret="CMZLmA8OeoTMUzVZLVnQcwoU3wJqWQ",
    user_agent="fundProject",
    password="welcome00",
    username="rorochabra",
)
prog_list = []

def append_arr_as_row(file_name, arr_elem, newline=''):
    with open(file_name, 'a+', newline='') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(arr_elem)

with open('reddit_list.csv', 'w', newline='') as write_arr:
    csv_writer = writer(write_arr)
    csv_writer.writerow(['Name','Subreddit Exists?', 'Number of Posts in Programming Subreddit', 'Number of Subscribers', 'Number of Active Subscribers'])

with open('github_list.csv', 'r') as ghub:
    csv_reader = reader(ghub)
    for row in csv_reader:
        prog_list.append(row[0])

prog_list.pop(0)
for prog in prog_list:
    prog_arr = [0]*4
    prog_arr[0] = prog
    try:
        sr_list = reddit.subreddits.search_by_name(query=prog, exact=True)
        prog_arr[1] = "Yes"
    except:
        prog_arr[1] = "No"   
    sub_count = 0
    for submission in reddit.subreddit("programming").search(prog, sort="comments", limit=None):
        sub_count += 1
    prog_arr[2] = sub_count
    if prog_arr[1] == "Yes":
        prog_arr[3] = "TBD"

    append_arr_as_row('reddit_list.csv', prog_arr)