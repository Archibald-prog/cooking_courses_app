# Обработка GET-запросов
class GetRequests:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        """
        Метод принимает параметры GET-запроса
        в формате строки и преобразует их в словарь
        :param data:
        :return:
        """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        # Получаем параметры запроса в формате строки
        query_string = environ['QUERY_STRING']
        # Преобразуем строку в словарь
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


# Обработка POST-запросов
class PostRequests:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        """
        Метод возвращает тело запроса в байтах
        :param env: словарь environ
        :return:
        """
        content_length_data = env.get('CONTENT_LENGTH')
        if content_length_data:
            content_length = int(content_length_data)
        else:
            content_length = 0
        if content_length > 0:
            data = env['wsgi.input'].read(content_length)
        else:
            data = b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # Декодируем данные запроса в строковый формат
            data_str = data.decode(encoding='utf-8')
            # Преобразуем данные из строки в словарь
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
