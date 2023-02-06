"""Проблема при перекрестном импорте(cross-import)."""


# Проблема параллельного импорта:
# from application import connection
#
#
# class Application:
#     def __init__(self, connection):
#         self.connection = connection
#
#     def start(self):
#         print(f"Приложение запущено и подключено к {self.connection}")
#
#
# app = Application(connection)


# Решение проблемы:
class Application:
    def __init__(self, connection):
        self.connection = connection

    def start(self):
        print(f"Приложение запущено и подключено к {self.connection}")
