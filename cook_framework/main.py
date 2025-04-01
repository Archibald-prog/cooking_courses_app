class PageNotFound404:
    def __call__(self, *args, **kwargs):
        return '404 WHAT', '404 PAGE not found'


class Framework:
    def __init__(self, routes_obj, fronts_obj):
        self.routes_obj = routes_obj
        self.fronts_obj = fronts_obj

    def __call__(self, environ, start_response):
        # Получаем роут, по которому пользователь выполнил переход
        path = environ['PATH_INFO']

        # Добавляем закрывающий слеш
        if not path.endswith('/'):
            path = f'{path}/'

        # Находим нужный контроллер -
        # как значение ключа path в словаре self.routes_obj
        if path in self.routes_obj:
            view = self.routes_obj[path]
        else:
            view = PageNotFound404()

        # Создаем словарь с данными запроса.
        # Заполняем словарь, передавая его фронт-контроллерам
        request = {}
        for front in self.fronts_obj:
            front(request)

        # Запускаем контроллер - получаем код и тело ответа.
        # Код ответа передаем в функцию start_response(),
        # тело ответа кодируем в байты.
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
