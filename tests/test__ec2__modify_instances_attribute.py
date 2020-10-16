import aws_scripts


def test_modify_instances_attribute():
    instances = aws_scripts.ec2.modify_instance_user_data(tags={'Cluster': 'oto-prod-ecs'})
    print(instances)


def test_empty_tags():
    errored = False
    try:
        instances = aws_scripts.ec2.modify_instance_attribute(tags={})
    except Exception as err:
        errored = True

    assert errored
