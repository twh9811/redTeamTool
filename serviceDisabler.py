import subprocess
import random


def get_services():
    output = subprocess.Popen(["systemctl", "--type=service", "--state=running"], stdout=subprocess.PIPE)
    output = output.stdout.read().decode()
    return output

def select_service(list_of_services_string):
    total_services = len(list_of_services_string)
    # Selects service randomly by line. Exclude 0 to skip headers
    service_number = random.randrange(1, total_services)
    service_list = list_of_services_string.split()
    selected_service_string = service_list[service_number]
    service_parts = selected_service_string.split()
    service_name = service_parts[0]
    return service_name
    
def main():
    services = get_services()
    service = select_service(services)
    print(service)

main()