import requests


url = 'https://ru.wttr.in/'
options = '?n?3?M?q?T'


for city in ('Лондон', 'Шереметьево', 'Череповец'):
    response = requests.get(url + f'/{city}{options}')
    print(response.text)
