
# Gen Token Function


import json
import time
import requests
from FMC_Token import get_token



def main():

    auth_token = get_token()
    server = "https://fmcrestapisandbox.cisco.com"
    headers = {'Content-Type': 'application/json'}
    headers['X-auth-access-token'] = auth_token

    api_path = "/api/fmc_platform/v1/info/serverversion"  # param
    url = server + api_path
    if (url[-1] == '/'):
        url = url[:-1]

    # GET OPERATION


    try:
        # REST call with SSL verification turned off:
        system_get = requests.get(url, headers=headers, verify=False)
        # REST call with SSL verification turned on:
        #r = requests.get(url, headers=headers, verify='/path/to/ssl_certificate')
        status_code = system_get.status_code
        resp = system_get.text
        if (status_code == 200):
            print("GET successful. Response data --> ")
            json_resp = json.loads(resp)
            print(json.dumps(json_resp, sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            system_get.raise_for_status()
            print("Error occurred in GET --> " + resp)
    except requests.exceptions.HTTPError as err:
        print("Error in connection --> " + str(err))
    finally:
        if system_get: system_get.close()


if __name__ == "__main__":
    main()
