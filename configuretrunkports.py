import netmiko
import sys
import time
from netmiko import ConnectHandler
ios_l2_corelayer = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.33',
    'username':'pythonauto',
    'password': 'python123',
    'secret': 'cisco'

}

ios_l2_distlayer1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.34',
    'username':'pythonauto',
    'password': 'python123',
    'secret': 'cisco'
}

ios_l2_distlayer2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.35',
    'username':'pythonauto',
    'password': 'python123',
    'secret': 'cisco'

}
ios_l2_accesslayer1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.36',
    'username':'pythonauto',
    'password': 'python123',
    'secret': 'cisco'
}

ios_l2_accesslayer2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.37',
    'username':'pythonauto',
    'password': 'python123',
    'secret': 'cisco'

}

ios_l2_accesslayer3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.38',
    'username':'pythonauto',
    'password': 'python123',
    'secret': 'cisco'

}

try:
    ssh_connection = ConnectHandler(**ios_l2_accesslayer1)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 0/0", "gig 0/1 ", "gig1/0"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)
        print(out)



except:
    print("login failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**ios_l2_distlayer1)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 0/0", "gig 0/1 ", "gig 0/2", "gig 2/1", "gig 2/0", "gig 1/0", "gig 1/1"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)
        print(out)
except:
    print("command failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**ios_l2_distlayer2)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 0/0", "gig 0/1 ", "gig 0/2", "gig 2/1", "gig 2/0", "gig 1/0", "gig 1/1"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)
        print(out)
except:
    print("command failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**ios_l2_corelayer)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 1/2", "gig 1/3 ", "gig 0/2", "gig 2/1", "gig 2/0", "gig 0/2", "gig 1/1"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)
        print(out)
except:
    print("command failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**ios_l2_accesslayer2)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 1/1", "gig 1/0 ", "gig 0/1", "gig 0/0", "gig 0/2", "gig 0/3"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)
        print(out)
except:
    print("command failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**ios_l2_accesslayer3)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 0/0", "gig 0/1 ", "gig 0/2", "gig 0/3", "gig 1/0", "gig 1/1"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)
        print(out)
except:
    print("command failure\n")
    sys.exit()
ssh_connection.disconnect()
