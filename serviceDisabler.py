import subprocess
import sys
# pip install psutil
import psutil

def main():
    cmd = 'systemctl --type=service --state=running'
    output = subprocess.Popen(cmd)
    print(output)

main()