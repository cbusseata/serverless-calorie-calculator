def get_variables(environment = 'local'):
    if environment.upper() == 'LOCAL':
        return {
            "api_base_url": "http://0.0.0.0:3000",
            "api_key": "local-test",
        }

    return {}
