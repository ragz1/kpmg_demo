import boto3
import json

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='XXXXXXX',
    aws_secret_access_key='XXXXXX',
    region_name='XXXXXX'
)

# Create an EC2 client
ec2_client = session.client('ec2')

# Specify the instance IDs for which you want to retrieve metadata
instance_ids = ['instance-id-1', 'instance-id-2', 'instance-id-3']

# Retrieve metadata for the specified EC2 instances
response = ec2_client.describe_instances(InstanceIds=instance_ids)

# Extract instance metadata from the response
instance_metadata = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        metadata = {
            'InstanceId': instance['InstanceId'],
            'InstanceType': instance['InstanceType'],
            'State': instance['State']['Name']
            # Add more fields as per your requirement
        }
        instance_metadata.append(metadata)

# Convert metadata to JSON format
json_metadata = json.dumps(instance_metadata, indent=4)

# Print or save the JSON metadata
print(json_metadata)






