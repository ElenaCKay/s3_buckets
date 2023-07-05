# S3 Simple storage service

Like blob storage in azure. Used to store content on the cloud in a robust way over multiple regions if you like. Instead of container it is bucket. Don't touch the buckets already there. The region is global.

Working on CRUD -> Create, Read, Update/Upload, Delete.

Install AWS CLI in pycharm

`pip install awscli`

`aws configure`

In here you give the details it needs and it will log you in.

`aws s3 ls` -> This will give you a list of all the buckets.

To make a bucket:
`aws s3 mb s3://tech241-elena-bucket --region eu-west-1`

To upload a file to a bucket:
`aws s3 cp testfile.txt s3://tech241-elena-bucket`
To check if it has worked you can go to the gui interface and click on the bucket and the file should be there.

To get the folder containing everything in the bucket:
`aws s3 sync s3://tech241-elena-bucket <folder name>
`
This is like doing a git clone but for buckets.

To delete the bucket you need to first delete what is inside. This is to delete a specific file:
`aws s3 rm s3://tech241-elena-bucket/<file name>
`

To delete everything inside the bucket
`aws s3 rm s3://tech241-elena-bucket --recursive`

Then delete the bucket:
`aws s3 rb s3://tech241-elena-bucket
`

S3 bucket documentation:
https://docs.aws.amazon.com/cli/latest/reference/s3/

High level commands:
https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-delete-buckets

## Scripting these principles

First step is to install boto3. `pip install boto3`
