import yaml
from netmiko import ConnectHandler


def send_show_command(dev,command):
    print(dev)

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:

        print(send_show_command(dev, command))