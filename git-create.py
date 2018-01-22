#!/usr/bin/python3

import requests
import sys
import json
from pprint import pprint as pp


def git_repos(name, key='xxxxxxxxxxxxxxxxxxxxx'):

    """****************************************************
 usage: ./git-create.py <repo name> <apikey>

 <repo name>: Name of the Repository to be created

 <apikey> OPTIONAL: Api key generated from Git account

 One line command to delete repo (Admin Rights required):
 curl -XDELETE -H 'Authorization: token <your api toke>' "https://api.github.com/repos/<username>/<repository name>"
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
        print('The repo --> {0} is successfully created \n'
              'The Clone ssh url is --> {1} \n'
              'The Clone HTTP url is --> {2}'.format(out['name'], out['ssh_url'], out['svn_url']))
    else:
        response = json.loads(resp.content.decode('utf-8'))
        raise ValueError("[?] Unexpected Response: [HTTP {0}]: Content: {1}".format(resp.status_code,
                                                                                    pp(response, indent=4)))

    return None


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(git_repos.__doc__)
        raise SyntaxError('Missing Argument')
        sys.exit()
    elif len(sys.argv) == 2:
        pp(sys.argv)
        repo_name = sys.argv[1]
        git_repos(repo_name)
        sys.exit()
    elif len(sys.argv) == 3:
        pp(sys.argv)
        repo_name = sys.argv[1]
        key = sys.argv[2]
        git_repos(repo_name, key)
    else:
        pp(git_repos.__doc__)
        raise SyntaxError('Incomplete or incorrect argument given as input')
        sys.exit()
