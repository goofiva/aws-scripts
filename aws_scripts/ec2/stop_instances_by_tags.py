import time
import boto3
import aws_scripts
from botocore.exceptions import ClientError

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
    #
    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = client.stop_instances(InstanceIds=instance_ids, DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

    print('Waiting for all instances to be stopped')

    while True:
        instances = aws_scripts.ec2.get_instances_by_tags(tags)
        all_stopped = True
        for instance in instances:
            instance_name = aws_scripts.ec2.instance.get_name(instance)
            if instance['State']['Name'] != 'stopped':
                print('%s is %s' % (instance_name, instance['State']['Name']))
                all_stopped = False

        if all_stopped:
            print('All instances stopped')
            break

        print('Sleeping for 10s')
        time.sleep(10)
