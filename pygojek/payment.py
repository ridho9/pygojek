from .base import request


def get_gopay_detail():
    options = {
        'method': 'GET'
    }

    return request(options, 'wallet/profile/detailed')


def get_gopay_history(page, limit):
    options = {
        'method': 'GET',
        'params': {
            'page': str(page),
            'limit': str(limit)
        }
    }
    return request(options, 'wallet/history')

def get_gopay_qr_id(phone):
    options = {
        'method': 'GET',
        'params': {
            'phone_number': str(phone),
        }
    }
    return request(options, 'wallet/qr-code')

def transfer_gopay(qr_id, amount, description, pin):
    options = {
        'method': 'POST',
        'body': {
            'qr_id': qr_id,
            'amount': amount,
            'description': description,
        },
        'headers': {
            'pin': pin
        }
    }
    return request(options, 'v2/fund/transfer')