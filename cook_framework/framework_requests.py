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
