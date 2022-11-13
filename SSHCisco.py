import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthentionException, ssh_exception, NetMikoTimeoutException

USERNAME = input("Please enter your SSH username: ")
PASS = getpass("Please enter your SSH password: ")

device = {
    'ip': {'192.168.1.10'},
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    f = open('backup.conf', 'x')
    f.write(output)
    f.close()
except (AuthentionException):
    print("An aunthentication error occured while connecting to:" + device[ip])
except (ssh_exception):
    print("An error occured while connecting to device " + device[ip] + "via ssh. Is SSH enabled?")
except (NetMikoTimeoutException):
    print("The device " = device[ip] + " timed out when attempting to connect")
