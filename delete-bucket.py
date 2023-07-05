import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket("tech241-elena-python-bucket")

response = bucket.delete()

print(response)