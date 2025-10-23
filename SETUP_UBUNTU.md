# Setup Instructions for Ubuntu VM

## Prerequisites
- Ubuntu 20.04 or later
- Python 3.8+ (usually pre-installed)
- Git installed

## Installation Steps

### 1. Clone Repository
```bash
git clone https://github.com/SassyxD/IPA2024-Final.git
cd IPA2024-Final
```

### 2. Install System Dependencies
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv sshpass
```

### 3. Create Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Python Packages
```bash
pip install -r requirements.txt
```

### 5. Setup Environment Variables
Create a file `set_env.sh`:
```bash
#!/bin/bash
export WEBEX_ACCESS_TOKEN="your_token_here"
export WEBEX_ROOM_ID="your_room_id_here"
export STUDENT_ID="66070061"
export ROUTER_IP="10.0.15.61"
```

Make it executable:
```bash
chmod +x set_env.sh
```

### 6. Configure Ansible
The `ansible.cfg`, `hosts`, and `playbook.yaml` files are already configured.

Make sure your router credentials are set in `playbook.yaml`:
- Username: admin
- Password: cisco

### 7. Run the Program
```bash
source set_env.sh
python3 ipa2024_final.py
```

## Testing Commands

Send these commands to your Webex Teams room:
- `/66070061 create` - Create loopback interface
- `/66070061 delete` - Delete loopback interface  
- `/66070061 enable` - Enable loopback interface
- `/66070061 disable` - Disable loopback interface
- `/66070061 status` - Check loopback status
- `/66070061 gigabit_status` - Check GigabitEthernet status
- `/66070061 showrun` - Backup router config using Ansible

## Troubleshooting

### SSH Connection Issues
If Ansible can't connect to router:
```bash
# Test SSH manually
ssh admin@10.0.15.61
```

### Ansible Issues
```bash
# Test Ansible connectivity
ansible all -m ping

# Run playbook manually
ansible-playbook playbook.yaml
```

## Moving to Another Computer

### Export Your Work
On current machine:
```bash
# Commit any changes
git add .
git commit -m "feat: working setup"
git push
```

### Import on New Machine
On new Ubuntu VM:
```bash
# Clone repository
git clone https://github.com/SassyxD/IPA2024-Final.git
cd IPA2024-Final

# Follow installation steps above
```

### Sync Environment Variables
Copy your environment variables from Windows to Ubuntu:
1. Copy values from Windows `set_env.ps1`
2. Create `set_env.sh` on Ubuntu with same values

## Continue GitHub Copilot Chat on Another Computer

### Method 1: Using GitHub Account
1. Install VS Code on new computer
2. Install GitHub Copilot extension
3. Sign in with same GitHub account
4. Open the cloned repository
5. Chat history is synced via your GitHub account

### Method 2: Fresh Start
If you want to start a new chat but keep context:
1. Push all code to GitHub first
2. Clone on new computer
3. Start new Copilot chat
4. Reference this README and other docs
5. Copilot will understand your codebase from the files

## Important Files to Keep Synced
- `requirements.txt` - Python dependencies
- `ansible.cfg` - Ansible configuration
- `hosts` - Ansible inventory
- `playbook.yaml` - Ansible playbook
- All `*_final.py` files - Your Python scripts
- `.env.example` - Template for environment variables
- `SETUP.md` / `SETUP_UBUNTU.md` - Documentation

## Notes
- Ansible works perfectly on Linux/Ubuntu
- No Python 3.13 compatibility issues on Ubuntu
- All features should work without modifications
