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
    ssh_connection = ConnectHandler(**ios_l2_corelayer)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())

    for n in range (2,7):
        print("creating via python vlan" + str(n))
        Command_Vlan = ['vlan' + str(n), 'name pythonvlan' + str(n)]
        out = ssh_connection.send_config_set(Command_Vlan)
        print(out)
        time.sleep(2)

except:
    print("login failure\n")
    sys.exit()

ssh_connection.disconnect()
distribution_and_access_layer_devices = [ios_l2_accesslayer1, ios_l2_accesslayer2, ios_l2_accesslayer3, ios_l2_distlayer1, ios_l2_distlayer2, ios_l2_corelayer]
for devices in distribution_and_access_layer_devices:
    try:
        ssh_connection = ConnectHandler(**devices)
        print("conection success")
        ssh_connection.enable()
        command = ['show vtp status', 'show vlan bri']
        out2 = ssh_connection.send_config_set(command)
        print(out2)
        time.sleep(1)
    except:
        print("failed to execute script\n")
        sys.exit()



