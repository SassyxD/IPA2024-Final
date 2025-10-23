import subprocess
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def showrun():
    # Get student ID from environment
    student_id = os.getenv('STUDENT_ID', '66070123')
    
    # read https://www.datacamp.com/tutorial/python-subprocess to learn more about subprocess
    command = [
        'ansible-playbook', 
        'playbook.yaml', 
        '-e', 
        f'ansible_student_id={student_id}'
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=120)
        output = result.stdout
        print("Ansible output:", output)
        
        # Check if tasks completed successfully
        if 'ok=2' in output and result.returncode == 0:
            return 'ok'
        else:
            print("Ansible error:", result.stderr)
            return 'Error: Ansible'
    except subprocess.TimeoutExpired:
        return 'Error: Ansible'
    except Exception as e:
        print(f"Error running ansible: {e}")
        return 'Error: Ansible'
