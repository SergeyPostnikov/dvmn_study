import requests


url = 'https://wttr.in/'
options = '?n?3?M?q?T?ru'


def main(*args=('Лондон', 'Шереметьево', 'Череповец')):
    for city in args:
        response = requests.get(f'{url}/{city}{options}')
        print(response.text)


if __name__ == '__main__':
    main()