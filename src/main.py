from utils import get_operations, get_last_five_operations, date, operation_to, operation_from

operations_list = get_last_five_operations(get_operations())

for oper in operations_list:

    oper_date = date(oper)
    oper_to = operation_to(oper)
    oper_from = operation_from(oper)
    oper_sum = oper["operationAmount"]["amount"]
    description = oper["description"]
    name = oper["operationAmount"]["currency"]["name"]
    print(f'{oper_date} {description}\n'
          f'{oper_from} -> {oper_to}\n'
          f'{oper_sum} {name}')
    print()