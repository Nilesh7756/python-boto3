#!/usr/bin/env python

import boto3
import sys

s3 = boto3.resource('s3')

for bucket_name in sys.argv[1:]:
    bucket = s3.Bucket(bucket_name)
    try:      
        response = bucket.delete()
        print response
    except Exception as error:
        print error
