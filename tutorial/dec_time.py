from datetime import datetime
import requests

def timeing(func):
    """get the time befor and after the result"""
    def inner(*args):
        print(datetime.now())
        func(*args) #You call anonymous func and args
        print(datetime.now())
    return inner

@timeing
def get_result(link):
    """check for the link exsisting"""
    response = requests.get(link)
    status = response.status_code
    if status == 200:
        print('Success')
    else:
        print('Not found')


get_result('https://www.google.com') #anf ACTION!!!



#IT WORKS !!!