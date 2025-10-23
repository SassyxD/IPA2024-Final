import subprocess
import os

def showrun():
    # read https://www.datacamp.com/tutorial/python-subprocess to learn more about subprocess
    # Set environment variables for Ansible
    env = os.environ.copy()
    
    command = ['ansible-playbook', 'playbook.yaml']
    result = subprocess.run(command, capture_output=True, text=True, env=env)
    result_output = result.stdout
    print(result_output)
    
    # Check if playbook executed successfully (ok=2 means both tasks succeeded)
    if 'ok=2' in result_output or 'ok=3' in result_output or 'ok=4' in result_output:
        return 'ok'
    else:
        return 'Error: Ansible'

