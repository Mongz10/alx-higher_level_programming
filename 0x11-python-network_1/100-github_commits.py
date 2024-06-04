#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Function that list 10 commits (from the most recent to oldest)
    of the repository.The first argument will be the repository name
    and the second argument will be the owner name
    """

    def print_commits(i, commit_list):
        """
        List the commits, less than 10 commits
        """
        sha = commit_list[i].get('sha')
        commit = commit_list[i].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print('{}: {}'.format(sha, name))


