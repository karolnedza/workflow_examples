#!/usr/bin/env python
"""Script to create a pull request on GitHub."""
import argparse
import os
import subprocess
import sys

import requests
from requests.auth import HTTPBasicAuth


GITHUB_API_URL = 'https://api.github.com'
GITHUB_API_TOKEN = os.environ.get('GITHUB_API_TOKEN')

def get_input_args():
    """Get the pull request information from the user."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--text',
        help='text to be sent to SNOW',
        default=None
    )
    parser.add_argument(
        '--file',
        help='Specify the file where the text context would be read and sent to SNOW',
        default=None
    )
    parser.add_argument(
        '--field',
        help='The SNOW record field to be updated',
        default=None
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

def sn_callback(input_args, data):
    """ Invoke sn callback """

    headers = {
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    response = requests.patch(
        input_args.sn_url, json=data, headers=headers, auth = HTTPBasicAuth(input_args.sn_user, input_args.sn_password)
    )
    if response.status_code != 200:
        print(response.json())
        sys.exit(1)

def main():
    """Run the script."""
    input_args = get_input_args()

    if input_args.field is None:
        field = "comments"
    else:
        field = input_args.field

    if input_args.text is not None:
        data = {
            f"{field}": f"{input_args.text}"
        }
    elif input_args.file is not None:
        txt_file = open(input_args.file)
        buffer = txt_file.read(1024)
        data = {
            f"{field}": f"{buffer}"
        }

    sn_callback(input_args, data)

if __name__ == '__main__':
    main()
