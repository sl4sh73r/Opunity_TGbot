from messages import *
from validators.seller import *


def validate_employment_type(data: str, error_message: str):
    if len(data) == 1:
        number = int(data)
        if number <= 0:
            raise Exception(error_message)
        return EMPLOYMENT_LIST[number - 1]
    elif len(data) > 1:
        data = data.replace(' ', '').lower()
        if data not in EMPLOYMENT_LIST:
            raise Exception(error_message)
        return data
    else:
        raise Exception(error_message)
    

def validate_person_info(data: str, employment_type: str, error_message: str):
    if employment_type == 'ип' or employment_type == 'самозанятый':
        if len(data.split(' ')) != 3:
            raise Exception(error_message)
        return data.capitalize()
    return data


def validate_inn(data: str, error_message: str):
    if not data.isnumeric():
        raise Exception(error_message)
    if len(data) != 10 and len(data) != 12:
        raise Exception(error_message)
    return int(data)
