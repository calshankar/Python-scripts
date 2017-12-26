#!/usr/bin/python3

import requests
import sys
import json
from pprint import pprint as pp


def git_repos(key, name):

    """****************************************************
 usage: ./git-create.py <repo name> <apikey>

 <repo name>: Name of the Repository to be created

 <apikey>   : Api key generated from Git account
****************************************************"""

    api_url_user = 'https://api.github.com/user/'
    api_token = key
    repo = {'name': str(name)}
    pp(repo)
    headers = {'Content-Type': 'application/json',
               'Authorization': 'token {0}'.format(api_token)}
    api_url = '{0}repos'.format(api_url_user)

    resp = requests.post(api_url, headers=headers, data=json.dumps(repo))

    if resp.status_code == 201:
        out = json.loads(resp.content.decode('utf-8'))
        pp('The repo --> {0} is successfully created & the clone url is --> {1}'.format(out['name'], out['git_url']), indent=4)
    else:
        response = json.loads(resp.content.decode('utf-8'))
        raise ValueError("[?] Unexpected Response: [HTTP {0}]: Content: {1}".format(resp.status_code,
                                                                                    pp(response, indent=4)))

    return None


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(git_repos.__doc__)
        raise SyntaxError('Missing Argument')
        sys.exit()
    elif sys.argv[1] is None or sys.argv[2] is None:
        pp(git_repos.__doc__)
        raise SyntaxError('Incomplete or incorrect argument given as input')
        sys.exit()
    else:
        api_key = sys.argv[1]
        repo_name = sys.argv[2]
        git_repos(repo_name, api_key)
