
import json
import requests
from FMC_Token import get_token



def main():

    auth_token = get_token()
    server = "https://fmcrestapisandbox.cisco.com"
    headers = {'Content-Type': 'application/json'}
    headers['X-auth-access-token'] = auth_token


    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/accessrules"
    url = server + api_path
    if (url[-1] == '/'):
        url = url[:-1]

    # POST OPERATION


    post_data ={
                  "action": "ALLOW",
                  "enabled": True,
                  "type": "AccessRule",
                  "name": "Shawki11",
                  "sendEventsToFMC": False,
                  "logFiles": False,
                  "logBegin": False,
                  "logEnd": False,
                  "variableSet": {
                    "name": "Default Set",
                    "id": "VariableSetUUID",
                    "type": "VariableSet"
                  },
                  "vlanTags": {
                    "objects": [
                      {
                        "type": "VlanTag",
                        "name": "vlan_tag_1",
                        "id": "VlanTagUUID1"
                      },
                      {
                        "type": "VlanTag",
                        "name": "vlan_tag_2",
                        "id": "VlanTagUUID2"
                      }
                    ]
                  },
                  "urls": {
                    "urlCategoriesWithReputation": [
                      {
                        "type": "UrlCategoryAndReputation",
                        "category": {
                          "name": "Weapons",
                          "id": "URLCategoryUUID",
                          "type": "URLCategory"
                        },
                        "reputation": "BENIGN_SITES_WITH_SECURITY_RISKS"
                      }
                    ]
                  },
                  "sourceZones": {
                    "objects": [
                      {
                        "name": "External",
                        "id": "SecurityZoneUUID",
                        "type": "SecurityZone"
                      }
                    ]
                  },
                  "destinationZones": {
                    "objects": [
                      {
                        "name": "Internal",
                        "id": "SecurityZoneUUID",
                        "type": "SecurityZone"
                      }
                    ]
                  },
                  "sourcePorts": {
                    "objects": [
                      {
                        "type": "ProtocolPortObject",
                        "name": "AOL",
                        "id": "ProtocolPortObjectUUID"
                      }
                    ]
                  },
                  "destinationPorts": {
                    "objects": [
                      {
                        "type": "ProtocolPortObject",
                        "name": "Bittorrent",
                        "id": "ProtocolPortObjectUUID"
                      }
                    ]
                  },
                  "ipsPolicy": {
                    "type": "IntrusionPolicy",
                    "id": "ipsPolicyUuid",
                    "name": "ipsPlicyName"
                  },
                  "filePolicy": {
                    "type": "FilePolicy",
                    "id": "filePolicyUuid",
                    "name": "filePolicyName"
                  },
                  "snmpConfig": {
                    "id": "snmpConfigUuid",
                    "name": "snmp_alert1",
                    "type": "SNMPAlert"
                  },
                  "syslogConfig": {
                    "id": "syslogConfigUuid",
                    "name": "syslog_alert1",
                    "type": "SyslogAlert"
                  },
                  "newComments": [
                    "comment1",
                    "comment2"
                  ]
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




