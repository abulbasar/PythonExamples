from boto3 import client, resource

import boto3
import os
from datetime import datetime

"""
You can get the access_key_id and access_key_secret from ~/.aws/credentials
file if aws cli is already configure, otherwise, 
you can generate a new id from aws web console.

"""

session = boto3.Session(
    aws_access_key_id="AKIAZHJXBAVUDQ7T3OMZ",
    aws_secret_access_key="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"
)

s3 = session.resource("s3")

bucket = s3.Bucket("abul.einext.com")

"""
for bucket in s3.buckets.all():
    print(bucket.name)
    
"""


dir_name = "/data/movielens"

for fname in os.listdir(dir_name):

    path = os.path.join(dir_name, fname)
    if os.path.isfile(path) and fname.endswith(".csv"):
        start_time = datetime.now()
        bucket.upload_file(path, f"movie-lens-2/{fname}")
        duration = (datetime.now() - start_time).microseconds/1000000
        print(f"Uploaded: {path} took: {duration} seconds")




