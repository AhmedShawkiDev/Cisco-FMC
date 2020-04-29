
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

    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks"
    #api_path = "/api/fmc_config/v1/domain/DomainUUID/object/networks"
    url = server + api_path
    if (url[-1] == '/'):
        url = url[:-1]

    # POST OPERATION
    #### Input the Data

    post_data = {
                      'name': 'Shawkiiii',
                      'value': '50.20.20.0/24',
                      'overridable': False,
                      'description': 'Test  Object',
                      'type': 'Network'
                    }

    #post_data = open('FMC_Create_net_input.txt').read()
    #print(post_data)
    try:
        # REST call with SSL verification turned off:
        Net_Post = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
        # REST call with SSL verification turned on:
        #Net_Post = requests.post(url, data=json.dumps(post_data), headers=headers, verify='/path/to/ssl_certificate')
        status_code = Net_Post.status_code

        # Wait 10 seconds after server responds
        print(f"Request accepted: status code {status_code}")
        time.sleep(10)

        resp = Net_Post.text
        print("Status code is: " + str(status_code))
        if status_code == 201 or status_code == 202:
            print("Post was successful...")
            json_resp = json.loads(resp)
            print(json.dumps(json_resp, sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            Net_Post.raise_for_status()
            print("Error occurred in POST --> " + resp)
    except requests.exceptions.HTTPError as err:
        print("Error in connection --> " + str(err))
    finally:
        if Net_Post: Net_Post.close()



if __name__ == "__main__":
    main()




