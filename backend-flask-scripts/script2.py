import requests

def check_udemy_status():
    url = "https://www.udemy.com/"
    response = requests.get(url)
    print(response)
    return response.status_code

check_udemy_status()
    
   