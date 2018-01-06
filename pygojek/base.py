from . import config
import requests

API_URL = 'https://api.gojekapi.com/'


def request(options: dict, url):
    get_url = API_URL + url
    headers = {
        'content-type': 'application/json',
        'X-AppVersion': config.get_app_version(),
        'X-UniqueId': config.unique_id,
        'X-Location': config.get_location(),
        'authorization': 'Bearer ' + config.get_token()
    }

    headers.update(options.get('headers', {}))

    if options['method'] == 'GET':
        r = requests.get(get_url, headers=headers, params=options.get('params', ''))
    elif options['method'] == 'POST':
        r = requests.post(get_url, headers=headers, json=options['body'])
    elif options['method'] == 'DELETE':
        r = requests.delete(get_url, headers=headers)
    else:
        return {'success': False, 'message': 'Bad parameters, please try again'}, 401

    ret_dict = {'status_code' : r.status_code}
    ret_dict.update(r.json())

    return ret_dict
