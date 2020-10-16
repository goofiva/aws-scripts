import sys
from termcolor import cprint

import boto3
import aws_scripts

client = boto3.client('ec2')


def modify_instance_user_data(tags: list, file_path: str, dry_run: bool=True) -> list:
    """

    :param tags:
        {'Cluster':'oto-prod-ecs'}
    :param file_path:
    :param dry_run:
    """
    instances = aws_scripts.ec2.get_instances_by_tags(tags)

    if len(instances) == 0:
        cprint('No instances found with the tags (%s)' % str(tags), 'red')
        sys.exit(1)

    if not dry_run:
        aws_scripts.ec2.stop_instances_by_tags(tags=tags)

    for instance in instances:
        if dry_run:
            cprint('Found instances with tags (%s)' % str(tags), 'green')
            instance_name = aws_scripts.ec2.instance.get_name(instance)
            print("    %s  %s" % (instance['InstanceId'], instance_name))

        elif not dry_run:
            instance_name = aws_scripts.ec2.instance.get_name(instance)
            client.modify_instance_attribute(
                InstanceId=instance['InstanceId'],
                UserData={
                    'Value': aws_scripts.helpers.encrypt.encode_base64(file_path)
                }
            )
            print('%s user data changed' % instance_name)
