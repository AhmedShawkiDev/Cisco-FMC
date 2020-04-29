#Retrieves, deletes, creates, or modifies the network objects associated with the specified ID. If no ID is specified for a GET, retrieves
# list of all network objects.
# Gen Token Function


import json
import requests
from FMC_Token import get_token



def main():

    auth_token = get_token()
    server = "https://fmcrestapisandbox.cisco.com"
    headers = {'Content-Type': 'application/json'}
    headers['X-auth-access-token'] = auth_token

    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks"
    url = server + api_path
    if (url[-1] == '/'):
        url = url[:-1]

    # GET OPERATION

    try:
        # REST call with SSL verification turned off:
        Net_Req = requests.get(url, headers=headers, verify=False)
        # REST call with SSL verification turned on:
        #r = requests.get(url, headers=headers, verify='/path/to/ssl_certificate')
        status_code = Net_Req.status_code
        resp = Net_Req.text
        if (status_code == 200):
            print("GET Networks successful. Response data ...... ")
            json_resp = json.loads(resp)
            print(json.dumps(json_resp, sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            Net_Req.raise_for_status()
            print("Error occurred in GET --> " + resp)
    except requests.exceptions.HTTPError as err:
        print("Error in connection --> " + str(err))
    finally:
        if Net_Req: Net_Req.close()


if __name__ == "__main__":
    main()





