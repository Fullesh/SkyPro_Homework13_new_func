def get_val(data, key=None, default=None):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    :param default: Дефолтное значение в случае если нет ключа
    :param key: Значение ключа в словаре
    :param data: получает на вход словарь
    :return: значение по ключу. Если ключ отсутствует, то выводится значение default
    """
    if key in data.keys():
        return data[key]
    else:
        return default
