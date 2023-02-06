"""Шаблон 'Singleton'."""


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print(f"Закрытие соединения с БД")

    def read(self):
        return "Данные из БД"

    def write(self, data):
        print(f"Запись в БД: {data}")


db = DataBase("root", "12345", 80)
db2 = DataBase("root2", "67890", 40)
print(id(db), id(db2))
