from messages import *


def validate_numeric_field(
        data: str, type: str, error_message: str
    ):
    if type == 'float':
        number = float(data)
    elif type == 'int':
        number = int(data)

    if number <= 0:
        raise Exception(error_message)
    return number


def validate_string_field(
        data: str, value_list: list, error_message: str
    ) -> str:
    while (data.count(' ') > 1):
        data = data.replace(' ', '', 1)
    data = data.lower()

    if len(data) == 1 or len(data) == 2:
        number = int(data)
        return value_list[number - 1]
    elif len(data) > 1:
        if data not in value_list:
            raise Exception(error_message)
        return data
    else:
        raise Exception(error_message)


def validate_post_processing(
        data: str, error_message: str
    ) -> int:
    if len(data) == 1:
        key = int(data)
        if key != 0 and key != 1:
            raise Exception(error_message)
        return key
    elif len(data) > 1:
        data = data.lower()
        if data == 'да':
            return 1
        elif data == 'нет':
            return 0
        else:
            raise Exception(error_message)
    else:
        raise Exception(error_message)
