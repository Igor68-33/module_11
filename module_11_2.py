# Интроспекция
from pprint import pprint
import inspect


def introspection_info(obj):
    result = dict()
    result.update({'type': str(type(obj)).split()[1][1:-2]})
    attributes = []
    method = []
    for attr_name in dir(obj):
        if hasattr(obj, attr_name):  # проверка наличия атрибута
            attributes.append(attr_name)
        if 'method' in str(type(getattr(obj, attr_name))):  # проверка наличия метода
            method.append(attr_name)
    # print(attr_name, getattr(obj, attr_name))
    # print('attributes:', attributes)
    # print('locals att:', locals()['attributes'])  # список атрибутов
    result['attributes:'] = locals()['attributes']
    # print('method:', method)
    # print('local_metod', locals()['method'])  # список методов
    result['method'] = locals()['method']
    # print('globals:', globals()['__name__'])
    # print('getmodule:', inspect.getmodule(obj))
    result['module'] = globals()['__name__']  # модуль основной
    result['getmodule'] = inspect.getmodule(obj)

    try:
        result['name'] = obj.__name__  # имя может отсутствовать
        # print('name:', obj.__name__)
        # print('dict:', obj.__dict__)
    except AttributeError as er:
        # print(er)
        result['name'] = er

    if str(type(obj)).split()[1] == "'function'>":  # для функции
        # print('getclosurevars:', inspect.getclosurevars(obj))
        result['getclosurevars'] = inspect.getclosurevars(obj)

        # print('getmembers:', '=' * 40)
    # pprint(inspect.getmembers(obj))
    # print('getmembers_static:', '-' * 40)
    # pprint(inspect.getmembers_static(obj))

    # print('ismodule:', inspect.ismodule(obj))
    # print('isclass:', inspect.isclass(obj))
    # print('isfunction:', inspect.isfunction(obj))
    # print('isbuiltin:', inspect.isbuiltin(obj))

    try:
        # print('signature:', inspect.signature(obj))
        result['signature'] = str(inspect.signature(obj))  # для выполняемых обектов
    except TypeError as er:
        # print(er)
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
print(number_info)
