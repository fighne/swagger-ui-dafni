from ruamel.yaml import YAML
import os
import sys


yaml=YAML()   # default, if not specfied, is 'rt' (round-trip)

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.yaml'):
            yaml_file = open(file, 'rb')
            yfile = yaml.load(yaml_file)
            yfile['host'] = 'localhost'
            yaml.dump(yfile, sys.stdout)
            