import yaml
import os
import json

def name_conv(file_name):
    return ( file_name.split('.')[0] ).replace('_', ' ')

def get_root_url(type_str, conf_json):
    return conf_json[type_str]['url']

url_config_file = "dafni.json"
if os.path.isfile(url_config_file):
    conf_json = json.loads( open(url_config_file, 'rb') )
else:
    conf_json = [ {""} ]
 
top = os.getcwd()

if "ROOT_URL_TYPE" in os.environ:
    root_url_type = os.environ.getenv('ROOT_URL_TYPE')
else:
    os.environ.putenv('ROOT_URL_TYPE', 'local')
    root_url_type = 'local'

 
yaml_list = [] 
for root, dirs, files in os.walk(top):
    for file in files:
        if file.endswith('.yaml'):
            ( yaml.load( open(file, 'rb') ) )['host'] = get_root_url(root_url_type, conf_json)
            t_dict = {}
            t_dict['url'] = "http://localhost/" + file
            t_dict['name'] = name_conv(file) 
            yaml_list.append(t_dict)

