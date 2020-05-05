def myDecorator(func):
    def wrapper():
        print('Обертка!')
        print(f'Оборачиваем функцию: {func}.')
        print('Выполняю функцию:')
        func()
        print('Закончили работать!')
    return wrapper


@myDecorator
def multiple():
    c = 5 * 4
    print(c)


def speedtest(func):
    import time

    def wrapper():
        start = time.time()

        func()

        finish = time.time()
        print(f'Прошло {finish - start} секунд.')
    return wrapper()


@speedtest
def searchinGoogle():
    import requests

    s = requests.get('https://google.com/')

searchinGoogle()