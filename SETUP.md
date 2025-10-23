# IPA2024-Final - Network Automation with Webex Teams

This project implements a Webex Teams bot that manages network device configurations using RESTCONF, Netmiko, and Ansible.

## Features

### Part 1 - Loopback Interface Management (RESTCONF)
- **create**: Create a loopback interface with student ID
- **delete**: Delete a loopback interface
- **enable**: Enable (no shutdown) a loopback interface
- **disable**: Disable (shutdown) a loopback interface
- **status**: Check the status of a loopback interface

### Part 2 - Advanced Operations
- **gigabit_status**: Check status of all GigabitEthernet interfaces (Netmiko)
- **showrun**: Backup running configuration (Ansible)

## Prerequisites

- Python 3.8 or higher
- Access to Cisco IOS XE router with RESTCONF/NETCONF enabled
- Webex Teams account and bot token
- Ansible installed

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SassyxD/IPA2024-Final.git
cd IPA2024-Final
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- Linux/Mac:
  ```bash
  source venv/bin/activate
  ```

4. Install required packages:
```bash
pip install -r requirements.txt
```

5. Install Ansible collection for Cisco IOS:
```bash
ansible-galaxy collection install cisco.ios
```

## Configuration

Set the following environment variables:

```powershell
# Windows PowerShell
$env:WEBEX_ACCESS_TOKEN = "your_webex_bot_token"
$env:WEBEX_ROOM_ID = "your_room_id"
$env:STUDENT_ID = "your_student_id"
$env:ROUTER_IP = "router_ip_address"
```

```bash
# Linux/Mac
export WEBEX_ACCESS_TOKEN="your_webex_bot_token"
export WEBEX_ROOM_ID="your_room_id"
export STUDENT_ID="your_student_id"
export ROUTER_IP="router_ip_address"
```

## Usage

1. Start the bot:
```bash
python ipa2024_final.py
```

2. Send commands to the Webex Teams room:
```
/[STUDENT_ID] create
/[STUDENT_ID] delete
/[STUDENT_ID] enable
/[STUDENT_ID] disable
/[STUDENT_ID] status
/[STUDENT_ID] gigabit_status
/[STUDENT_ID] showrun
```

Example:
```
/66070123 create
```

## Project Structure

```
IPA2024-Final/
├── ipa2024_final.py       # Main program with Webex Teams integration
├── restconf_final.py      # RESTCONF operations
├── netmiko_final.py       # Netmiko operations
├── ansible_final.py       # Ansible automation
├── backup_config.yml      # Ansible playbook for config backup
├── hosts                  # Ansible inventory
├── ansible.cfg            # Ansible configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Technologies Used

- **RESTCONF**: Interface configuration management
- **Netmiko**: Interface status checking with TextFSM
- **Ansible**: Configuration backup automation
- **Webex Teams API**: Bot messaging and file sharing

## License

This project is for educational purposes as part of IPA2024 Final Exam.

## Author

- Student ID: [Your Student ID]
- GitHub: https://github.com/SassyxD/IPA2024-Final
