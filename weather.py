import requests


def main():
    cities = ('Лондон', 'Шереметьево', 'Череповец')
    url = 'https://wttr.in/'
    options = {
        "lang": "ru",
        "n": "", 
        "M": "", 
        "q": "", 
        "T": "",  
    }

    for city in cities:
        response = requests.get(f'{url}/{city}', params=options)
        response.raise_for_status()
        print(response.text)
    


if __name__ == '__main__':
    main()