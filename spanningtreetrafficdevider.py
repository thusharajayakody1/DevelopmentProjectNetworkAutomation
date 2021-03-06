import netmiko
import sys
import time
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import ssh_exception
from netmiko import NetMikoTimeoutException

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

deviceslist = [ios_l2_distlayer1]
# making distribution layer 1 switch root bridge for odd vlans and secondary route for even vlans
for devices in deviceslist:
    try:
        ssh_connection = ConnectHandler(**devices)
        print("connection success\n")
    except(NetMikoAuthenticationException):
        print('Authentification failure:' + str(devices))
        continue
    except(NetMikoTimeoutException):
        print('timeout to device')
        continue
    except(EOFError):
        print('end of file while attempting to connect device')
        continue
    except(ssh_exception):
        print('Cant establish ssh tunnel. please check ssh server status')
        continue
    except Exception as unknown_error:
        print('cannot identify the specific error please check config of the devices')
        continue

    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    commandos = ['spanning-tree mode rapid-pvst', 'spanning-tree vlan 1,3,5,7 priority 0',
                 'spanning-tree vlan 2,4,6 priority 4096']
    outputs = ssh_connection.send_config_set(commandos)
    print(outputs)
    time.sleep(10)
# configuring ether channels on dlw1


    ssh_connection.disconnect()

deviceslist2 = [ios_l2_distlayer2]
for device in deviceslist2:
    try:
        ssh_connection2 = ConnectHandler(**device)
        print('connection successful')

    except(NetMikoAuthenticationException):
        print('Authentification failure:' + str(devices))
        continue
    except(NetMikoTimeoutException):
        print('timeout to device')
        continue
    except(EOFError):
        print('end of file while attempting to connect device')
        continue
    except(ssh_exception):
        print('Cant establish ssh tunnel. please check ssh server status')
        continue
    except Exception as unknown_error:
        print('cannot identify the specific error please check config of the devices')
        continue
    ssh_connection2.enable()
    print(ssh_connection2.find_prompt())
    ssh_connection2.enable()
    commands = ['spanning-tree mode rapid-pvst', 'spanning-tree vlan 2,4,6 priority 0',
                'spanning-tree vlan 1,3,4,6 priority 4096']

    out = ssh_connection2.send_config_set(commands)
    print(out)
    file = open("pythonvlanscriptOutput.txt", "w+")
    file.write(''.join(out))
    file.close()

    #configure the etherchannel ports



    ssh_connection2.disconnect()
sys.exit()



















