"""Проблема при перекрестном импорте(cross-import)."""
# Проблема параллельного импорта:
# from classes import app
#
# connection = {
#     "uri": "myconnection",
#     "password": "mysecretpassword"
# }
#
# app.start()

# Решение проблемы:
from factory import create_app

connection = {
    "uri": "myconnection",
    "password": "mysecretpassword"
}

app = create_app(connection)
app.start()
