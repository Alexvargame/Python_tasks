import yaml
from jinja2 import Environment, FileSystemLoader

def generate_config(template_file,data):
    env = Environment(loader=FileSystemLoader("."))
    templ = env.get_template(template_file)
    return templ.render(data)

def create_vpn_config(template1,template2,data_dict):
    env=Environment(loader=FileSystemLoader("."))
    templ1=env.get_template(template1)
    print(templ1.render(data_dict))
    env = Environment(loader=FileSystemLoader("."))
    templ1 = env.get_template(template2)
    print(templ1.render(data_dict))

def main():

    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(data)
    print(generate_config(template_file, data))
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    data_file='data_files/router_info.yml'
    with open(data_file) as f:
        data=yaml.safe_load(f)
    print(generate_config('templates/cisco_base.txt',data))
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    data_file = 'data_files/add_vlan_to_switch.yaml'
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config('templates/add_vlan_to_switch.txt', data))
    print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    data = {
        'tun_num': 10,
        'wan_ip_1': '192.168.100.1',
        'wan_ip_2': '192.168.100.2',
        'tun_ip_1': '10.0.1.1 255.255.255.252',
        'tun_ip_2': '10.0.1.2 255.255.255.252'
    }
    create_vpn_config('templates/gre_ipsec_vpn_1.txt','templates/gre_ipsec_vpn_2.txt',data)

if __name__ == "__main__":
    main()

#
