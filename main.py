# main.py
from fetching_data import fetch_xml_data
from converter import convert_xml_to_json
from uploader import upload_to_s3

if __name__ == "__main__":
    url = "https://www.w3schools.com/xml/simple.xml"
    bucket = "your-bucket-name"
    file_name = "output_data.json"

    xml_data = fetch_xml_data(url,"","")
    json_data = convert_xml_to_json(xml_data)
    print(json_data)
    # -upload_to_s3(json_data, bucket, file_name)
