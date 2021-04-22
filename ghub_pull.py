import time
from github import Github
from csv import writer
from array import *
import datetimeeeimport calendar
t0 =  time.time()

counter = 0
g = Github('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')
repo_arr = [0]*10

time.sleep(3)
stars_lower = input("Lower Stars Range: ")
stars_higher = input("Higher Stars Range: ")
forks = input('Minimum Forks: ')
created = input('Created by (YYYY-MM-DD): ')

query = 'stars:' + stars_lower + '..' + stars_higher + ' forks:>' + forks + ' created:>' + created

with open('github_list.csv', 'w', newline='') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(['Name', 'Stars', 'Forks', 'Closed Pulls Count', 'Open Pulls Count', 
        'Number of Commits', 'Days Since Last Commit', 'Number of Contributors', 'Number of Workflow Runs', 'Topics'])

def append_arr_as_row(file_name, arr_elem, newline=''):
    with open(file_name, 'a+', newline='') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(arr_elem)

def get_commit_date(repo):
    commits = repo.get_commits()
    data = commits.get_page(0)
    last_commit = data[0].commit.author.date.date()
    today = datetime.datetime.now().date()
    elapsed_time = today - last_commit
    commit_date = str(elapsed_time)
    days = commit_date.split(' ')
    return days[0], commits.totalCount


for repo in g.search_repositories(query, 'stars', 'desc'):
    if (g.get_rate_limit().core.remaining == 0):
        core_rate_limit = g.get_rate_limit().core
        reset_time = calendar.timegm(core_rate_limit.reset.timetuple())
        sleep_time = reset_time - calendar.timegm(time.gmtime()) + 5
        print("Sleeping for: " + str(sleep_time) + ' seconds')
        time.sleep(sleep_time)
    repo_arr[0] = repo.name
    repo_arr[1] = repo.stargazers_count
    repo_arr[2] = repo.forks
    repo_arr[3] = repo.get_pulls(state='closed', sort='created', direction='asc').totalCount
    repo_arr[4] = repo.get_pulls(state='open', sort='created', direction='asc').totalCount
    repo_arr[5] = get_commit_date(repo)[1]
    repo_arr[6] = get_commit_date(repo)[0]
    repo_arr[7] = repo.get_contributors().totalCount
    repo_arr[8] = repo.get_workflow_runs().totalCount
    # repo_arr[9] = repo.get_topics()
    counter += 1
    print(counter)
    append_arr_as_row('github_list.csv', repo_arr)

t1 = time.time()

print("=====================")
print("Complete - " + str(round(t1-t0, 2)) + ' secs')
print("=====================")


