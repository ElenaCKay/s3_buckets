# first thing is to import boto3 library
import boto3

# set up s3 connection
s3 = boto3.client('s3')

# create a bucket, in the eu-west-1 region - Two parameters; the name and the location
bucket_name = s3.create_bucket(Bucket="tech241-elena-python-bucket", CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})

# print bucket name to confirm working script
print(bucket_name)
print(type(bucket_name))