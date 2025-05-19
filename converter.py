# converter.py
import xmltodict
import json

def convert_xml_to_json(xml_data):
    data_dict = xmltodict.parse(xml_data)
    return json.dumps(data_dict, indent=4)
