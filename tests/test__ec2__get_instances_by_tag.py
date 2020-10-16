import aws_scripts


def test_get_instances_by_tag():
    instances = aws_scripts.ec2.get_instances_by_tags(tags={'Cluster': 'oto-prod-ecs'})
    print(instances)


def test_empty_tags():
    errored = False
    try:
        instances = aws_scripts.ec2.get_instances_by_tags(tags={})
    except Exception as err:
        errored = True

    assert errored
