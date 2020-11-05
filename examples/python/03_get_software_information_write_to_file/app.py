from jnpr.junos import Device
from pprint import pprint
import requests
import json

devices = [
        "192.168.43.201",
        "192.168.43.202",
        "192.168.43.203",
        "192.168.43.204",
        "192.168.43.205",
        "192.168.43.206"
    ]


def write_to_file(device, payload):
    # Open function to open the file "hostname.py" 
    # (same directory) in append mode 
    filename = f"./output/{device}.py"
    file1 = open(filename,"a")
    file1.write(str(payload) + "\n")
    file1.close()
    pass


for device in devices:
    with Device(host=device, user='ansible', password='hol-leap!bru6PSOO') as dev:
        try:
            show_version = dev.rpc.get_software_information({'format':'json'})
            write_to_file(device, show_version)
        except:
            pass
