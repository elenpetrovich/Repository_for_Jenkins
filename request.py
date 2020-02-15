# авторизация на сайте
# out_page.html - записывается страница после авторизации
# answer.txt - содержит ответ

import requests
from requests.auth import HTTPBasicAuth


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