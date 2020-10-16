import sys
from termcolor import cprint

import boto3
from botocore.exceptions import ClientError
import aws_scripts

client = boto3.client('ec2')


def modify_instance_user_data_by_tags(tags: list, file_path: str, dry_run: bool=True) -> list:
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
        instance_name = aws_scripts.ec2.instance.get_name(instance)
        if dry_run:
            cprint('Found instances with tags (%s)' % str(tags), 'green')
            print("    %s  %s" % (instance['InstanceId'], instance_name))

        elif not dry_run:
            try:
                client.modify_instance_attribute(
                    InstanceId=instance['InstanceId'],
                    DryRun=True,
                    UserData={
                        'Value': aws_scripts.helpers.get_file_content(file_path)
                        # 'Value': aws_scripts.helpers.encrypt.encode_base64(file_path)
                    }
                )
            except ClientError as e:
                if 'DryRunOperation' not in str(e):
                    raise

            status = client.modify_instance_attribute(
                InstanceId=instance['InstanceId'],
                UserData={
                    'Value': aws_scripts.helpers.get_file_content(file_path)
                    # 'Value': aws_scripts.helpers.encrypt.encode_base64(file_path)
                }
            )
            print(status)
            cprint('%s user data changed successful.' % instance_name, 'green')
