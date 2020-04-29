
import json
import requests
from FMC_Token import get_token



def main():

    auth_token = get_token()
    server = "https://fmcrestapisandbox.cisco.com"
    headers = {'Content-Type': 'application/json'}
    headers['X-auth-access-token'] = auth_token

    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"  # param
    url = server + api_path
    if (url[-1] == '/'):
        url = url[:-1]

    # POST OPERATION


    post_data = {
                  "type": "AccessPolicy",
                  "name": "AccessPolicy-Shawki-test-1",
                  "defaultAction": {
                    "action": "BLOCK"
                  }
                }
    try:

        # REST call with SSL verification turned off:
        r = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
        # REST call with SSL verification turned on:
        #r = requests.post(url, data=json.dumps(post_data), headers=headers, verify='/path/to/ssl_certificate')
        status_code = r.status_code
        resp = r.text
        print("Status code is: " + str(status_code))
        if status_code == 201 or status_code == 202:
            print("Post was successful...")
            json_resp = json.loads(resp)
            print(json.dumps(json_resp, sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            r.raise_for_status()
            print("Error occurred in POST --> " + resp)
    except requests.exceptions.HTTPError as err:
        print("Error in connection --> " + str(err))
    finally:
        if r: r.close()


if __name__ == "__main__":
    main()





