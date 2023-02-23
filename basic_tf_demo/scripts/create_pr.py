#!/usr/bin/env python
"""Script to create a pull request on GitHub."""
import argparse
import os
import subprocess
import sys

import requests


GITHUB_API_URL = 'https://api.github.com'
GITHUB_API_HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
}
GITHUB_API_TOKEN = os.environ.get('GITHUB_API_TOKEN')


def get_pr_info():
    """Get the pull request information from the user."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--head-branch',
        '--head',
        '--h',
        help='The branch that contains commits for your pull request.',
        required=True
    )
    parser.add_argument(
        '--base-branch',
        '--base',
        '--b',
        help='The branch into which you want the pull request merged.',
        default="main"
    )
    #parser.add_argument('title', help='The title of the pull request')
    #parser.add_argument('body', help='The body of the pull request')
    return parser.parse_args()

def get_repo_info():
    """Get the repository information.

    Uses git config to get the remote URL and parses it to get the repository.
    The URL can take a few different forms:

        git@github.com:<repo_owner>/<repo_name>.git
        https://github.com/<repo_owner>/<repo_name>.git
        https://x-access-token:<token>@github.com/<repo_owner>/<repo_name>.git

    where we want to extract the string "<repo_owner>/<repo_name>".

    Returns:
        A string in the form <repo_owner>/<repo_name>
    """
    remote_url = subprocess.check_output(
        ['git', 'config', '--get', 'remote.origin.url']
    ).strip()

    if remote_url.startswith('git@'):
        repo_info = remote_url.split(':')[-1].replace('.git', '')
    elif remote_url.startswith('https://'):
        repo_name = remote_url.split('/')[-1].replace('.git', '')
        repo_owner = remote_url.split('/')[-2]
        repo_info = f'{repo_owner}/{repo_name}'
    else:
        raise ValueError(f'Unknown remote URL: {remote_url}')

    return repo_info


#def create_pr(repo_name, base_branch, head_branch, title, body):
def create_pr(repo_name, base_branch, head_branch):
    """Create the pull request on GitHub."""
    url = f'{GITHUB_API_URL}/repos/{repo_name}/pulls'
    data = {
        'base': base_branch,
        'head': head_branch,
        #'title': title,
        #'body': body
    }
    response = requests.post(
        url, json=data, headers=GITHUB_API_HEADERS, auth=(GITHUB_API_TOKEN, '')
    )
    return response


def main():
    """Run the script."""
    repo_name = get_repo_info()
    pr_info = get_pr_info()
    #response = create_pr(repo_name, pr_info.base_branch, pr_info.head_branch, pr_info.title, pr_info.body)
    response = create_pr(repo_name, pr_info.base_branch, pr_info.head_branch)
    if response.status_code != 201:
        print(response.json())
        sys.exit(1)

if __name__ == '__main__':
    main()
