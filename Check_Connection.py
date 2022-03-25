from urllib.request import urlopen

def Check_Connection():
    try:
        urlopen('http://www.google.com', timeout = 1)
        return True
    except:
        return False