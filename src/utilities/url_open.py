import requests
from bs4 import BeautifulSoup

def url_open(url):
    '''Url Opener and beautifulSoup creater object'''
    try:
        response = requests.get(url).text
        data_object = BeautifulSoup(response, 'html5lib')
    except Exception as e:
        print(e)
    else:
        return data_object
        print(data_object)