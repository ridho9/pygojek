from .base import request
from . import config

def getCustomerInfo():
    """
    Usage :
        p = pygojek.getCustomerInfo()
    Get the costumer info
    :return: requests object
    """
    options = {
        'method' : 'GET'
    }

    return request(options, '/gojek/v2/customer')
