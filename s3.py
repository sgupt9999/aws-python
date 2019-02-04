#!/usr/local/bin/python3.6

import boto3
import sys
import uuid

def create_bucket_name(bucket_prefix):
## Create a random bucket name with a given prefix
	print(current_region)
	return ''.join([bucket_prefix,str(uuid.uuid4())])

def create_temp_file(size, file_name,file_content):
	random_file_name = ''.join([str(uuid.uuid4().hex[:6]),file_name])
	with open(random_file_name,'w') as f:
		f.write(str(file_content) * size)
	return random_file_name

def bucket_exists(bucket):
## check if this bucket already exists
	client = boto3.client('s3')
	response = client.list_buckets()
	for bucket2 in response['Buckets']:
		if bucket2['Name'] == bucket:
			return True
	return False

def list_objects(bucket):
## List all the objects and size in a given bucket
	client = boto3.client('s3')
	response = client.list_objects_v2(Bucket=bucket)
	if 'Contents' in response.keys():
		for object in response['Contents']:
			print(object['Key'],'---------',object['Size'])
	else:
		print('The %s bucket has no objects'%bucket)

def delete_objects(bucket):
## Delete all objects in a given bucket
	client = boto3.client('s3')
	response = client.list_objects_v2(Bucket=bucket)
	if 'Contents' in response.keys():
		for object in response['Contents']:
			print('Deleting ',object['Key'])
			resonse_delete = client.delete_object(Bucket=bucket,Key=object['Key'])
	else:
		print('The %s bucket has no objects'%bucket)

print(bucket_exists('cmei-test-ohio'))
list_objects('cmei-test-ohio')
delete_objects('cmei-test-ohio')
list_objects('cmei-test-ohio')

sys.exit(0)


session = boto3.session.Session()
current_region = session.region_name
client = boto3.client('s3')
response = client.create_bucket(Bucket=create_bucket_name('xxx'),CreateBucketConfiguration={'LocationConstraint':current_region})
print(response)


first_file_name = create_temp_file(300,'firxtfile.txt','f')
print(first_file_name)

