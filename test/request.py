import requests
from requests.auth import HTTPBasicAuth
import os.path


def main():
    s = requests.session()
    email = 'weheweh197@nwesmail.com'
    password = 'ilh2uhbweipfh'
    url = 'https://stackoverflow.com/users/login'
    user_data = {'email': email, 'password': password}

    req = requests.get(url, auth=HTTPBasicAuth(email, password))
    response = s.post(url, data=user_data)

    file = open('out_page.html', 'wb')
    file.write(response.content)
    file.close()

    file = open('answer.txt', 'w')
    file.write(str(req))
    file.close()


def file_answer():
    main()
    file_path = "answer.txt"
    if (os.path.exists(file_path) == True):
        f = open('answer.txt', 'r')
        return str(f.read())
    else:
        return str("error")

def file_path():
    file_path = "out_page.html"
    return os.path.exists(file_path)