import subprocess
import random


def get_services():
    output = subprocess.Popen(["systemctl", "--type=service", "--state=running"], stdout=subprocess.PIPE)
    output = output.stdout.read().decode()
    return output

def select_service(list_of_services_string):
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
    process = subprocess.Popen(["systemctl", "disable", service_name])
    process.Popen.communicate()
    
def main():
    services = get_services()
    service = select_service(services)
    print(service, "is being disabled")
    disable_service(service)

main()