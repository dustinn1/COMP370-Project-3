import config

from github import Github
import csv

g = Github(login_or_token=config.access_token, per_page=100)


def getCodeSize(sha):
    size = 0
    tree = g.get_repo(
        "ninja-build/ninja").get_git_tree(sha).tree
    for element in tree:
        if (element.type == "blob"):
            size += element.size
        else:
            size += getCodeSize(element.sha)
    return size


with open('code_sizes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Sha", "Date", "Code Size"])
    for commit in g.get_repo("ninja-build/ninja").get_commits():
        writer.writerow(
            [commit.commit.committer.date, commit.commit.tree.sha, getCodeSize(commit.commit.tree.sha)])
