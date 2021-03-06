import time
import sys
import boto3
import aws_scripts
from botocore.exceptions import ClientError
from termcolor import cprint

client = boto3.client('ec2')

def stop_instances_by_tags(tags: dict, wait_till_done: bool=True):
    """

    :param tags:
    :param wait_till_done:
    :return:
    """
    instances = aws_scripts.ec2.get_instances_by_tags(tags)
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    try:
        client.stop_instances(InstanceIds=instance_ids, DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = client.stop_instances(InstanceIds=instance_ids, DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
        sys.exit(1)


    if wait_till_done:
        cprint('Waiting for all instances to be stopped', 'green')

        while True:
            instances = aws_scripts.ec2.get_instances_by_tags(tags)
            all_stopped = True
            for instance in instances:
                instance_name = aws_scripts.ec2.instance.get_name(instance)
                if instance['State']['Name'] != 'stopped':
                    cprint('%s is %s' % (instance_name, instance['State']['Name']), 'green')
                    all_stopped = False

            if all_stopped:
                cprint('All instances stopped', 'green')
                break

            cprint('Sleeping for 10s', 'yellow')
            time.sleep(10)
