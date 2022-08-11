import requests

def get_weather(url, options, city):
    response = requests.get(f'{url}/{city}', params=options)
    response.raise_for_status()
    print(response.text)


def main():
    cities = ('Лондон', 'Шереметьево', 'Череповец')
    url = 'https://wttr.in/'
    options = {
        "lang": "ru",
        "n": "", # узкая версия (только день и ночь)
        "M": "", # показывать скорость ветра в м/с
        "q": "", # тихая версия (без текста "Прогноз погоды")
        "T": "", # отключить терминальные последовательности (без цветов) 
    }

    for city in cities:
        get_weather(url, options, city)
        


if __name__ == '__main__':
    main()