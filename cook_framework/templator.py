from os.path import join
from jinja2 import Template


def render(template_name, folder='templates', **kwargs):
    file_path = join(folder, template_name)
    with open(file_path, encoding='utf-8') as f:
        # получаем шаблон в формате строки
        # и передаем его в конструктор класса Template
        template = Template(f.read())
    # вызываем метод render класса Template,
    # передавая ему словарь с контекстом -
    # получаем рез-т рендеринга в строковом формате
    return template.render(**kwargs)
