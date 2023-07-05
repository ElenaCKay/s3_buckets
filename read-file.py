import boto3

s3 = boto3.client('s3')

key = 'newtestfile.txt'

downloaded_file = s3.download_file('tech241-elena-python-bucket', key, 'testfile.txt')

print(downloaded_file)


