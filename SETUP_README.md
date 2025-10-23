# IPA2024 Final Project

## Setup Instructions

### 1. Clone and Setup Virtual Environment
```bash
git clone <your-repo-url>
cd IPA2024-Final
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux  
source venv/bin/activate
```

### 2. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your details:
```bash
cp .env .env.local
```

Edit `.env` with your information:
```env
# Webex Teams Bot Token
WEBEX_BOT_TOKEN=your_webex_bot_token_here

# Router Configuration (from assigned spreadsheet)
ROUTER_IP=10.0.15.61
ROUTER_USERNAME=admin
ROUTER_PASSWORD=cisco

# Your Student ID
STUDENT_ID=66070123

# Webex Team Room ID  
WEBEX_ROOM_ID=your_room_id_here
```

### 4. Update Ansible Inventory
Edit `hosts` file with your assigned router IP:
```ini
[routers]
router1 ansible_host=<YOUR_ROUTER_IP>
```

## Usage

### Running the Main Program
```bash
python ipa2024_final.py
```

### Supported Commands (send to Webex Teams room)
- `/[STUDENT_ID] create` - Create loopback interface
- `/[STUDENT_ID] delete` - Delete loopback interface  
- `/[STUDENT_ID] enable` - Enable loopback interface
- `/[STUDENT_ID] disable` - Disable loopback interface
- `/[STUDENT_ID] status` - Check loopback interface status
- `/[STUDENT_ID] gigabit_status` - Check GigabitEthernet interfaces status
- `/[STUDENT_ID] showrun` - Backup running configuration

### Example Commands
```
/66070123 create
/66070123 status
/66070123 gigabit_status
/66070123 showrun
```

## File Structure
```
├── ipa2024_final.py      # Main program
├── restconf_final.py     # RESTCONF functions
├── netmiko_final.py      # Netmiko functions
├── ansible_final.py      # Ansible functions
├── playbook.yaml         # Ansible playbook
├── hosts                 # Ansible inventory
├── ansible.cfg          # Ansible configuration
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md           # This file
```

## Important Notes
1. Make sure your router IP is correct in both `.env` and `hosts` files
2. Ensure Webex Bot Token and Room ID are properly configured
3. Router must have NETCONF/RESTCONF enabled on ports 830/443
4. Use username `admin` and password `cisco` for router authentication

## Troubleshooting
- If imports fail, ensure virtual environment is activated and libraries are installed
- If router connection fails, verify IP address and network connectivity
- If Webex messages don't send, check Bot Token and Room ID
- For Ansible errors, verify `hosts` file configuration