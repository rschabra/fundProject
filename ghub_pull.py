import time
from github import Github
from csv import writer
from array import *

t0 =  time.time()

g = Github('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')
repo_arr = [0]*5

with open('github_list.csv', 'w') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(['Name', 'Stars', 'Forks', 'Closed Pulls Count', 'Open Pulls Count'])

def append_arr_as_row(file_name, arr_elem):
    with open(file_name, 'a+', newline='') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(arr_elem)

for repo in g.search_repositories('stars:4000..4500 forks:>10 created:>2018-01-01', 'stars', 'desc'):
    repo_arr[0] = repo.name
    repo_arr[1] = repo.stargazers_count
    repo_arr[2] = repo.forks
    repo_arr[3] = repo.get_pulls(state='closed', sort='created', direction='asc').totalCount
    repo_arr[4] = repo.get_pulls(state='open', sort='created', direction='asc').totalCount
    append_arr_as_row('github_list.csv', repo_arr)


t1 = time.time()

print("=====================")
print("Complete - " + str(t1-t0))
print("=====================")


