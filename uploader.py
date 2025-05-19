# uploader.py
import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(json_data, bucket_name, file_name):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Body=json_data, Bucket=bucket_name, Key=file_name)
        print("Upload successful")
    except NoCredentialsError:
        print("AWS credentials not found")
