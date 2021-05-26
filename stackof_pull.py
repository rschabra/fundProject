from csv import *
from array import *
from stackapi import StackAPI
import time
import datetime
import calendar
# import ghub_pull

SITE = StackAPI('stackoverflow')
prog_list = []

def append_arr_as_row(file_name, arr_elem, newline=''):
    with open(file_name, 'a+', newline='') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(arr_elem)

def days_since(time):
    today = datetime.datetime.now().date()
    elapsed_time = today - time
    question_date = str(elapsed_time)
    days = question_date.split(' ')
    return days[0]

with open('stackof_list.csv', 'w', newline='') as write_arr:
    csv_writer = writer(write_arr)
    csv_writer.writerow(['Name','Questions Asked', 'Questions Answered', 'Days since Last Question'])

with open('github_list.csv', 'r') as ghub:
    csv_reader = reader(ghub)
    for row in csv_reader:
        prog_list.append(row[0])

prog_list.pop(0)

for prog in prog_list:
    prog_arr = [0]*4
    questions = SITE.fetch('questions', tagged=prog)
    prog_arr[0] = prog
    prog_arr[1] = len(questions['items'])
    if (prog_arr[1] != 0):
        prog_arr[2] = prog_arr[1]
        for q in questions['items']:
            if (q['is_answered'] == False):
                prog_arr[2] = prog_arr[2] - 1
            if (q['last_activity_date'] > prog_arr[3]):
                prog_arr[3] = q['last_activity_date']
        prog_arr[3] = days_since(datetime.date.fromtimestamp(prog_arr[3]))

    append_arr_as_row('stackof_list.csv', prog_arr)
