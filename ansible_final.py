import subprocess
import os
import platform

def showrun():
    """
    ใช้ Ansible playbook เพื่อสำรองการตั้งค่าจาก router
    รองรับทั้ง Linux/Ubuntu และ Windows
    """
    try:
        # ตรวจสอบ OS และใช้ ansible-playbook ที่เหมาะสม
        if platform.system() == "Windows":
            # บน Windows ใช้ ansible-playbook จาก PATH (ต้องติดตั้งใน WSL หรือ Cygwin)
            ansible_cmd = "ansible-playbook"
        else:
            # บน Linux/Ubuntu ใช้ ansible-playbook ตรงๆ
            ansible_cmd = "ansible-playbook"
        
        # รัน Ansible playbook
        result = subprocess.run(
            [ansible_cmd, "playbook.yaml"],
            capture_output=True,
            text=True,
            env=os.environ.copy()
        )
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        if result.returncode == 0:
            return 'ok'
        else:
            return 'Error: Ansible'
    except FileNotFoundError:
        print("Error: ansible-playbook not found. Please install Ansible.")
        print("Ubuntu: sudo apt install ansible")
        print("Windows: Use WSL or run on Linux VM")
        return 'Error: Ansible not installed'
    except Exception as e:
        print(f"Error running ansible playbook: {e}")
        return 'Error: Ansible'

