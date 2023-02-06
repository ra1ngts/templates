"""С помощью шаблона factory(фабрика) решаем проблему с перекрестным импортом(cross-import)."""

from classes import Application


def create_app(connection):
    app = Application(connection)
    return app


