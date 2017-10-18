token = ''
location = '-6.175386, 106.827122'
uniqueId = '9774d56d682e549c'
appVersion = '2.28.2'
clientSecret = '83415d06-ec4e-11e6-a41b-6c40088ab51e'

def setToken(t):
    global token
    token = t

def getToken():
    return token

def setLocation(l):
    global location
    location = l

def getLocation():
    return location

def getAppVersion():
    return appVersion

def getUniqueId():
    return uniqueId
