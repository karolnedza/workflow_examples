#!/usr/bin/env python
"""Script to create a pull request on GitHub."""
import argparse
import os
import subprocess
import sys
import json

import requests
from requests.auth import HTTPBasicAuth


GITHUB_API_URL = 'https://api.github.com'
GITHUB_API_TOKEN = os.environ.get('GITHUB_API_TOKEN')

def get_input_args():
    """Get the pull request information from the user."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--merge',
        help='merge info string: e.g., "owner/repo-name,pull-request-id"',
        required=True
    )
    parser.add_argument(
        '--sn_url',
        help='SNOW callback URL'
    )
    parser.add_argument(
        '--sn_user',
        help='SNOW user name'
    )
    parser.add_argument(
        '--sn_password',
        help='SNOW password'
    )
    return parser.parse_args()

def merge_pr(repo_name, pr_no, input_args):
    """Create the pull request on GitHub."""
    url = f'{GITHUB_API_URL}/repos/{repo_name}/pulls/{pr_no}/merge'
    headers = {
        "Accept":"application/vnd.github+json",
        'Authorization': f'Bearer {GITHUB_API_TOKEN}'
    }
    data = {
        'commit_title': "SNOW",
        'title': f"PR {pr_no}: Create VPC and spoke",
    }
    response = requests.put(
        url, json=data, headers=headers
    )
    if response.status_code != 200:
        res = response.json()
        print(response.json())
        data = {
            "comments": json.dumps(res),
            "state": "Closed Incomplete"
        }
        sn_callback(input_args.sn_url, input_args.sn_user, input_args.sn_password, data)
        sys.exit(1)

def sn_callback(url, user, password, data):
    """ Invoke sn callback """

    headers = {
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    response = requests.patch(
        url, json=data, headers=headers, auth = HTTPBasicAuth(user, password)
    )
    if response.status_code != 200:
        print(response.json())
        sys.exit(1)

def main():
    """Run the script."""
    input_args = get_input_args()
    repo_name, pr = input_args.merge.split(",")
    merge_pr(repo_name, pr, input_args)

    data = {
        "comments": f"Merged PR {pr}"
    }
    sn_callback(input_args.sn_url, input_args.sn_user, input_args.sn_password, data)

if __name__ == '__main__':
    main()
