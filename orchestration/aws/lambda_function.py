# AWS Lambda function to fix network issues.

import boto3


def lambda_handler(event, context):
    ec2 = boto3.client("ec2")
    instance_id = event["instance_id"]

    # Restart instance
    ec2.reboot_instances(InstanceIds=[instance_id])
    return {"statusCode": 200, "body": f"Instance {instance_id} rebooted."}
