from github import Github

g = Github('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')

for repo in g.get_user().get_repos():
    print(repo.name)