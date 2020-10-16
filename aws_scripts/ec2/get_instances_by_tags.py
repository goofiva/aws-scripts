import boto3

client = boto3.client('ec2')


def convert_tags_list_to_dict(tags: list) -> dict:
    """

    :param tags:
    :return:
    """
    out_dict = {}
    for tag in tags:
        out_dict[tag['Key']] = tag['Value']
    return out_dict


def get_instances_by_tags(tags: dict) -> dict:
    """

    :param tags:
        {'key_1': 'value_1', 'key2': 'value_2'}
    :return:
    """

    if tags == {}:
        raise Exception('no_tags_specified')

    instances = client.describe_instances()
    out_instances = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_tags = convert_tags_list_to_dict(instance['Tags'])

            passed = True
            for tag_key in tags.keys():
                if tag_key in instance_tags.keys():
                    if tags[tag_key] != instance_tags[tag_key]:
                        passed = False
                else:
                    passed = False

            if passed:
                out_instances.append(instance)

    return out_instances
