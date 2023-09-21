import subprocess
import sys
# pip install psutil
import psutil

def main():
    output = subprocess.Popen(['ps', '-A'])
    print(output)

main()