from github import Github
from csv import writer
from array import *

g = Github('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')
repo_arr = [0]*5

def append_arr_as_row(file_name, arr_elem):
    with open(file_name, 'a+', newline='') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(arr_elem)

for repo in g.search_repositories('stars:2000..4000 forks:>100 created:>2018-01-01', 'stars', 'desc'):
    repo_arr[0] = repo.name
    repo_arr[1] = repo.stargazers_count
    repo_arr[2] = repo.forks
    repo_arr[3] = repo.open_issues_count
    repo_arr[4] = repo.watchers_count
    append_arr_as_row('github_list.csv', repo_arr)


