from ruamel.yaml import YAML
import os
import sys
import json

def name_conv(file_name):
    return ( file_name.split('.')[0] ).replace('_', ' ')

def get_root_url(type_str, conf_json):
    return conf_json[type_str]

yaml=YAML()   # default, if not specfied, is 'rt' (round-trip)

url_config_file = "dafni.json"
if os.path.isfile(url_config_file):
    conf_json = json.load( open(url_config_file, 'r', encoding='utf-8') )
else:
    conf_json = { 'local': 'localhost'} 
 
top = os.getcwd()

if "ROOT_URL_TYPE" in os.environ:
    root_url_type = os.environ['ROOT_URL_TYPE']
else:
    os.environ.putenv('ROOT_URL_TYPE', 'local')
    root_url_type = 'local'

 
yaml_list = [] 
for root, dirs, files in os.walk(top):
    for file in files:
        if file.endswith('.yaml'):
            yaml_file = open(file, 'rb')
            yfile = yaml.load(yaml_file)
            host_path = get_root_url(root_url_type, conf_json)
            yfile['host'] = host_path
            t_dict = {}
            t_dict['url'] = host_path + "/" + file
            t_dict['name'] = name_conv(file) 
            yaml_list.append(t_dict)
            with open(file, 'w') as swagger_file:
                yaml.dump(yfile, swagger_file)
            
with open('dafni-config.json', 'w') as file_pointer:
    json.dump(yaml_list, file_pointer)