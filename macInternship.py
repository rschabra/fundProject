from github import Github

g = Github('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')

for repo in g.search_repositories('stars:3500..4000 forks:>100', 'stars', 'desc'):
    print(repo.name + ', Stars: ' + str(repo.stargazers_count) + ', Forks: ' + str(repo.forks))