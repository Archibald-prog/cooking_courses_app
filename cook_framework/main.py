import quopri
from framework_requests import GetRequests, PostRequests


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

        # Создаем словарь с данными запроса
        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'Нам пришел POST-запрос: {Framework.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'Нам пришли GET-параметры: {request_params}')

        # Находим нужный контроллер -
        # как значение ключа path в словаре self.routes_obj
        if path in self.routes_obj:
            view = self.routes_obj[path]
        else:
            view = PageNotFound404()

        # for front in self.fronts_obj:
        #     front(request)

        # Запускаем контроллер - получаем код и тело ответа.
        # Код ответа передаем в функцию start_response(),
        # тело ответа кодируем в байты.
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
