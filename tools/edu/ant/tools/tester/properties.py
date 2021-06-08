import os

import yaml

file_name = "application-local.yml"
file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(file_dir)
file_location = parent_dir + "/resources/top_secret/"


def get_properties():
    with open(file_location + file_name) as file:
        properties = yaml.load(file, Loader=yaml.FullLoader)
    return properties
