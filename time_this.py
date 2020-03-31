import time


class Stopwatch:

    def __init__(self):
        """
        Конструктор класса
        """

        self.time = self.time_this

    def start(self, run="True"):
        """
        Эксперементировал c созданию секундомера
        """
        now = time.time()
        while run:
            t1 = time.time()
            stopwatch = t1 - now
            print(stopwatch)
            # return stopwatch

    def __enter__(self):
        """
        Планирую открыть через неё класс при помощи контекстного
        менеджера
        """
        self = self.time_this
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        планирую закрыть
        """
        pass




    def time_this(self, num_runs):

        def decorator(func):
            avg_time = 0

            for i in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()


                avg_time += t1 - t0

                print("количество запусков - ", i+1)
            avg_time = avg_time / num_runs

            print("Усредненное выполнение функции заняло %.5f секунд" % avg_time)

        return decorator

# Создаём сущьность
# avg = Stopwatch()

# Через атрибут time вызываем функцию time_this, в скобках указываем
# num_runs(количество попыток)
# @avg.time(10)
# def f():
#     for j in range(10000000):
#         pass

# Запуск секундомера
# avg.start()

# вызываем функцию через контекстный менеджер
with Stopwatch() as timer:
    @timer(10)
    def f():
        for j in range(10000000):
            pass



