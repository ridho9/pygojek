token = ''
location = '-6.175386, 106.827122'
unique_id = '9774d56d682e549c'
app_version = '2.28.2'
client_secret = '83415d06-ec4e-11e6-a41b-6c40088ab51e'

def set_token(t):
    global token
    token = t

def get_token():
    return token

def set_location(l):
    global location
    location = l

def get_location():
    return location

def get_app_version():
    return app_version

def get_uniqueid():
    return unique_id

def get_client_secret():
    return client_secret