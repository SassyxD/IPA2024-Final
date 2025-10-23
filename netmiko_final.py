from netmiko import ConnectHandler
from pprint import pprint
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

device_ip = os.getenv('ROUTER_IP', '10.0.15.61')
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}


def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("show ip interface brief", use_textfsm=True)
        interface_names = []
        
        for interface in result:
            interface_name = interface.get('INTF', '')
            interface_status = interface.get('STATUS', '').lower()
            
            if interface_name.startswith('GigabitEthernet'):
                interface_names.append(f"{interface_name} {interface_status}")
                if interface_status == "up":
                    up += 1
                elif interface_status == "down":
                    down += 1
                elif interface_status == "administratively down":
                    admin_down += 1
        
        # Create the response string
        interface_list = ", ".join(interface_names)
        summary = f" -> {up} up, {down} down, {admin_down} administratively down"
        ans = interface_list + summary
        
        pprint(ans)
        return ans
