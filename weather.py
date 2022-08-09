import requests


url = 'https://wttr.in/'
options = {
    "lang": "ru",
    "n": "",
    "3": "",
    "M": "",
    "q": "",
    "T": "",
} 



def main(cities=('Лондон', 'Шереметьево', 'Череповец')):
    for city in cities:
        response = requests.get(f'{url}/{city}', params=options)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()