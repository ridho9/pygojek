from . import config
import requests

API_URL = 'https://api.gojekapi.com'


def request(options, url):
    getURL = API_URL + url
    headers = {
        'content-type': 'application/json',
        'X-AppVersion': config.getAppVersion(),
        'X-UniqueId': config.uniqueId,
        'X-Location': config.getLocation(),
        'authorization': 'Bearer ' + config.getToken()
    }

    if options['method'] is 'GET':
        return requests.get(getURL, headers=headers)
