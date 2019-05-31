import boto3

def get_variables(environment = 'local'):
    """Dynamically retrieves variables for use in robot acceptance testing.

    Args:
        environment (string): The environment to retrieve variables for

    Returns:
        dict: Dictionary of variable names/values
    """
    if environment.upper() == 'LOCAL':
        return {
            'api_key': 'local-test',
            'api_base_url': 'http://0.0.0.0:3000',
        }

    return {
        'api_key': get_api_key(environment),
        'api_base_url': get_base_url(environment),
    }

def get_api_key(environment):
    """Retrieves the API key for the environment

    Args:
        environment (string): The environment to retrieve variables for

    Returns:
        string: API key

    Raises:
        Exception: If we cannot find the API key
    """
    client = boto3.client('apigateway', region_name='us-east-1')

    api_key_name = 'calorie-calculator-'+environment.lower()+'-test'

    response = client.get_api_keys()
    if not response['items']:
        raise Exception('No API keys!')

    for item in response['items']:
        if item['name'] == api_key_name:
            our_item = item
            break

    if not our_item:
        raise Exception('API key not found!')

    response = client.get_api_key(
        apiKey=our_item['id'],
        includeValue=True
    )

    if not response['value']:
        raise Exception('Error getting API key value!')

    return response['value']

def get_base_url(environment):
    """Retrieves the base URL for the REST API for the environment

    Args:
        environment (string): The environment to retrieve variables for

    Returns:
        string: base URL

    Raises:
        Exception: If we cannot find the necessary info for generating the URL
    """
    client = boto3.client('apigateway', region_name='us-east-1')

    rest_api_name = environment.lower()+'-calorie-calculator'

    response = client.get_rest_apis()
    if not response['items']:
        raise Exception('No REST apis!')

    for item in response['items']:
        if item['name'] == rest_api_name:
            our_item = item
            break

    if not our_item:
        raise Exception('REST API not found!')

    return 'https://%s.execute-api.us-east-1.amazonaws.com/%s' % (our_item['id'], environment.lower())
