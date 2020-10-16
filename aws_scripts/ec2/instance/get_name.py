
def get_name(instance):
    for tag in instance['Tags']:
        if tag['Key'] == 'Name':
            return tag['Value']
