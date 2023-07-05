import boto3

s3 = boto3.resource('s3')

file = 'newtestfile.txt'
bucket = 'tech241-elena-python-bucket'

s3.Object(bucket, file).delete()

print(f"{file} has been deleted from {bucket}")