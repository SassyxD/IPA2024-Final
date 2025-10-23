import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

requests.packages.urllib3.disable_warnings()

# Get configuration from environment variables
ROUTER_IP = os.getenv('ROUTER_IP', '10.0.15.61')
STUDENT_ID = os.getenv('STUDENT_ID', '66070123')

# Router IP Address is from environment variable
api_url = f"https://{ROUTER_IP}/restconf/data/ietf-interfaces:interfaces/interface=Loopback{STUDENT_ID}"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
basicauth = ("admin", "cisco")


def create():
    # Calculate IP address based on student ID
    last_three_digits = STUDENT_ID[-3:]  # Get last 3 digits
    if len(last_three_digits) == 3:
        x = int(last_three_digits[0])
        y = int(last_three_digits[1:])
    else:
        x = 0
        y = int(last_three_digits)
    
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": f"Loopback{STUDENT_ID}",
            "description": f"Loopback interface for student {STUDENT_ID}",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": f"172.{x}.{y}.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        }
    }

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return f"Interface loopback {STUDENT_ID} is created successfully"
    elif(resp.status_code == 409):
        print('Conflict - Interface already exists: {}'.format(resp.status_code))
        return f"Cannot create: Interface loopback {STUDENT_ID}"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return f"Cannot create: Interface loopback {STUDENT_ID}"


def delete():
    resp = requests.delete(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return f"Interface loopback {STUDENT_ID} is deleted successfully"
    elif(resp.status_code == 404):
        print('Not Found - Interface does not exist: {}'.format(resp.status_code))
        return f"Cannot delete: Interface loopback {STUDENT_ID}"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return f"Cannot delete: Interface loopback {STUDENT_ID}"


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": f"Loopback{STUDENT_ID}",
            "enabled": True
        }
    }

    resp = requests.patch(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return f"Interface loopback {STUDENT_ID} is enabled successfully"
    elif(resp.status_code == 404):
        print('Not Found - Interface does not exist: {}'.format(resp.status_code))
        return f"Cannot enable: Interface loopback {STUDENT_ID}"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return f"Cannot enable: Interface loopback {STUDENT_ID}"


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": f"Loopback{STUDENT_ID}",
            "enabled": False
        }
    }

    resp = requests.patch(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return f"Interface loopback {STUDENT_ID} is shutdowned successfully"
    elif(resp.status_code == 404):
        print('Not Found - Interface does not exist: {}'.format(resp.status_code))
        return f"Cannot shutdown: Interface loopback {STUDENT_ID}"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return f"Cannot shutdown: Interface loopback {STUDENT_ID}"


def status():
    api_url_status = f"https://{ROUTER_IP}/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback{STUDENT_ID}"

    resp = requests.get(
        api_url_status, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        interface_state = response_json.get('ietf-interfaces:interface', {})
        admin_status = interface_state.get('admin-status', '').lower()
        oper_status = interface_state.get('oper-status', '').lower()
        
        if admin_status == 'up' and oper_status == 'up':
            return f"Interface loopback {STUDENT_ID} is enabled"
        elif admin_status == 'down' or oper_status == 'down':
            return f"Interface loopback {STUDENT_ID} is disabled"
        else:
            return f"Interface loopback {STUDENT_ID} is disabled"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return f"No Interface loopback {STUDENT_ID}"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return f"No Interface loopback {STUDENT_ID}"
