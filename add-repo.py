#!/usr/bin/env python3

import requests, json, argparse, sys, colorama

## DATA
urlbase="https://api.bitbucket.org/2.0/repositories/"
login_user=""
login_pass=""
user="mrmilu"
repo=""
private_mode=True
create_project=True
project=""
project_key= ""


## CODE
if create_project:
    urlbase_project= "https://api.bitbucket.org/2.0/teams/"
    payload_project = { "name": project }
    post_project = requests.put(urlbase_project + "/".join([user, "projects", project_key]),
                       auth=(login_user, login_pass),
                       data=json.dumps(payload_project),
                       headers = {'content-type': 'application/json'})
    if post_project.ok:
        print(colorama.Fore.GREEN + "Se ha creado el proyecto:")
        print(post_project.json())
        print()
    else:
        print(colorama.Fore.RED + "ERROR: no se ha creado el proyecto")
        print(colorama.Fore.RED + post_project.json())
        sys.exit()


payload = {"accountname": user,
           "repo_slug": repo,
           "is_private": private_mode,
           "project": { "key": project_key }
           }

post = requests.post(urlbase + "/".join([user, repo]),
                   auth=(login_user, login_pass),
                   data=json.dumps(payload),
                   headers = {'content-type': 'application/json'})

if post.ok:
    print(colorama.Fore.GREEN + "Se ha creado el repo:")
    print(post.json())
    print()
    print(colorama.Fore.CYAN + "SSH = " + post.json()['links']['clone'][1]['href'] )
    print(colorama.Fore.CYAN + "HTTP = " + post.json()['links']['html']['href'] )
else:
    print(colorama.Fore.RED + "ERROR: no se ha creado el repo")
    print(post.json())
