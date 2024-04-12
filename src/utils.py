import json
# import zipfile
from _datetime import datetime

"""Распаковываем архив и достаем файл json с операциями"""


# file_zip = zipfile.ZipFile('operations.zip', 'r')
# file_zip.extractall('./')
# file_zip.close()


def get_operations():
    """Получаем список операций"""
    with open("operations.json", encoding="utf-8") as file:
        operations_list = json.load(file)
        return operations_list


def get_last_five_operations(operations_list):
    """Получаем список последних пяти операций"""
    operations_list_executed = [oper for oper in operations_list if oper != {} and oper['state'] == "EXECUTED"]
    operations_list_executed_sorted = sorted(operations_list_executed, key=lambda x: x["date"], reverse=True)
    last_five_operations_list = operations_list_executed_sorted[:5]
    return last_five_operations_list


def date(operation):
    """Возвращает информацию о дате операции"""
    operation_date_str = operation['date']
    operation_date = datetime.strptime(operation_date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return operation_date.strftime("%d.%m.%Y")


def operation_from(operation):
    """Возвращает информацию о счете списания"""
    if "from" in operation.keys():
        operat_from = operation["from"].split(" ")
        if len(operat_from) == 2:
            return (f'{operat_from[0]} {operat_from[1][:4]} '
                    f'{operat_from[1][4:6]}** **** {operat_from[1][-4:]}')
        elif len(operat_from) == 3:
            return (f'{operat_from[0]} {operat_from[1]} {operat_from[2][:4]} '
                    f'{operat_from[2][4:6]}** **** {operat_from[2][-4:]}')


def operation_to(operation):
    """Возвращает информацию о счете зачисления"""
    operat_to = operation["to"].split(" ")
    if len(operat_to) == 2:
        return f'{operat_to[0]} **{operat_to[1][-4:]}'
    elif len(operat_to) == 3:
        return f'{operat_to[0]} {operat_to[1]} **{operat_to[2][-4:]}'
