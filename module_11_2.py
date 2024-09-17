# Интроспекция
from pprint import pprint
import inspect


def introspection_info(obj):
    # словарь результатов
    result = dict()
    # определяем тип объекта
    result.update({'type': str(type(obj)).split()[1][1:-2]})
    # список атрибутов
    attributes = []
    # список методов
    methods = []

    for attr_name in dir(obj):
        # проверка наличия атрибута
        if hasattr(obj, attr_name):
            attributes.append(attr_name)
        # проверка наличия метода
        if 'method' in str(type(getattr(obj, attr_name))):
            methods.append(attr_name)

        # содержимое атрибута можно посмотреть
        # print(attr_name, getattr(obj, attr_name))

    # список атрибутов в результат запишем без методов
    result['attributes:'] = sorted(list(set.difference(set(attributes), set(methods))))
    # print('locals att:', locals()['attributes'])  # список атрибутов вариант 2

    # список методов в результат
    result['methods'] = methods
    # print('result['method'] =local_metod', locals()['method'])  # список методов вариант 2

    # имя текущего модуля
    result['module'] = globals()['__name__']  # модуль основной
    result['getmodule'] = inspect.getmodule(obj)  # характеристика модуля

    # имя может отсутствовать
    try:
        result['name'] = obj.__name__
        # print('name:', obj.__name__)
        # print('dict:', obj.__dict__)
    except AttributeError as er:
        # print(er)
        result['name'] = er

    # для функции переменные
    if str(type(obj)).split()[1] == "'function'>":
        # print('getclosurevars:', inspect.getclosurevars(obj))
        result['getclosurevars'] = inspect.getclosurevars(obj)

    # для выполняемых объектов сигнатура
    try:
        result['signature'] = str(inspect.signature(obj))
    except TypeError as er:
        result['signature'] = er

    return result


class Some_class:
    attrib1 = 50
    attrib2 = ['два', 'три']

    def __init__(self, number):
        self.number = number

    def test(self):
        pass


def some_function(a, b, c=10):
    print(some_int)
    pass


some_list = [1, 'два', (3, 3.1)]
some_str = 'my-string'
some_int = 12
var1 = Some_class(42)
number_info = introspection_info(some_function)
pprint(number_info)
