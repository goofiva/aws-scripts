import aws_scripts


def test_stop_instances_by_tags():
    instances = aws_scripts.ec2.start_instances_by_tags(tags={'Name': 'oto-prod_jumpbox'})


def test_empty_tags():
    errored = False
    try:
        instances = aws_scripts.ec2.start_instances_by_tags(tags={})
    except Exception as err:
        errored = True

    assert errored
