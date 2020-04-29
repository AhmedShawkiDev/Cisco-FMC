#!/usr/bin/env python


"""
Author: Ahmed Shawki
Purpose:  Python "requests" to get an access token from
Cisco FMC  using the REST API.
"""

import sys
import requests


def get_token():

    try:
        #for sandbox us the below link
        #server = "https://fmcrestapisandbox.cisco.com"
        server = input(" What is server-IP: ")
        username = input(" What is username: ")
        if len(sys.argv) > 1:
            username = sys.argv[1]
        password = input(" What is Password: ")
        if len(sys.argv) > 2:
            password = sys.argv[2]
        #auth_resp = None
        headers = {'Content-Type': 'application/json'}
        api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
        auth_url = server + api_auth_path
        auth_resp = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username, password), verify=False)
        auth_resp.raise_for_status()
        auth_headers = auth_resp.headers
        auth_token = auth_headers.get('X-auth-access-token', default=None)

        if auth_token == None:
            print("auth_token not found. Exiting...")
            sys.exit()
    except Exception as err:
        print("Error in generating auth token --> " + str(err))
        sys.exit()
    headers['X-auth-access-token'] = auth_token
    return auth_token

def main():
    """
    Execution begins here.
    """
    auth_token = get_token()
    print(auth_token)

#this is to ensure that the main is called whenever this module is run
if __name__ == "__main__":
    main()

