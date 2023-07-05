import boto3

# need an s3 variable, bucket variable, response variable
s3 = boto3.client('s3')

# methods

bucket_name = 'tech241-elena-python-bucket'
file_name = "testfile.txt"
new_file_name = "newtestfile.txt"

s3.upload_file(file_name, bucket_name, new_file_name)

#print response
print(f"{file_name} has been copied into {bucket_name} as {new_file_name}")