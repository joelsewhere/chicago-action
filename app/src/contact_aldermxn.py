

data = {}

def ContactAldermxn(ward):
    for aldermxn in data:
        if ward == aldermxn['ward']:
            return (aldermxn['name'], aldermxn['email'])
    return ('No data present', 'Test Data')