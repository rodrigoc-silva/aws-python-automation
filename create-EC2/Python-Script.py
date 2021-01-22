
import os
import tempfile

import boto3
from PIL import Image

s3 = boto3.client('s3')
DEST_BUCKET = os.environ['DEST_BUCKET']
SIZE = 128, 128

def lambda_handler(event, context):
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']