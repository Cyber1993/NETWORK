# pip install netmiko

from pprint import pprint
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

def send_show_command(device, command):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)

if __name__ == "__main__":
    device = {
        'device_type': 'cisco_ios',
        'host': '*.*.*.*',
        'username': '*********',
        'password': '*****************',
        'port': 22,
    }

while True:
    command = input("Введіть команду: * sh * * sho * * show *  ").strip().lower()

    if command.startswith(("sh", "sho", "show")):
        result = send_show_command(device, command)
        pprint(result, width=120)
    else:
        print("Команда повинна починатися з  * sh * * sho * * show * ")
