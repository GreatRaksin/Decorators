def speedtest(iterations):
    def decor(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0

            for i in range(iterations):
                start = time.time()
                values = func(*args, **kwargs)
                finish = time.time()
                total = total + (finish - start)
            print(f'Cреднее время исполнения: {total / iterations} секунд.')

            return values

        return wrapper
    return decor