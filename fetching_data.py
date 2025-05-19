# fetcher.py
import requests
from requests.auth import HTTPBasicAuth

def fetch_xml_data(url, username, password):
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

