import pytest
from src.utils import date, operation_to, operation_from, get_last_five_operations


@pytest.fixture
def utils_fixture():
    return [{"id": "1", "date": "07.01.2024", "state": "EXECUTED"},
            {"id": "2", "date": "01.01.2024", "state": "CANCELED"},
            {"id": "3", "date": "03.01.2024", "state": "CANCELED"},
            {"id": "4", "date": "02.01.2024", "state": "EXECUTED"},
            {"id": "5", "date": "04.01.2024", "state": "EXECUTED"},
            {"id": "6", "date": "06.01.2024", "state": "EXECUTED"},
            {"id": "7", "date": "05.01.2024", "state": "EXECUTED"}]


@pytest.fixture
def fixture_1():
    operation_test_1 = {'date': '2000-12-08T22:46:21.935582',
                        'operationAmount': {'amount': '41096.24',
                                            'currency': {'name': 'USD', 'code': 'USD'}},
                        'description': 'Открытие вклада',
                        'to': 'Счет 90424923579946435907'}
    return operation_test_1


@pytest.fixture
def fixture_2():
    operation_test_2 = {'date': '2001-11-19T09:22:25.899614',
                        'operationAmount': {'amount': '30153.72',
                                            'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод организации',
                        'from': 'Maestro 7810846596785568',
                        'to': 'MasterCard 6783917276771847'}
    return operation_test_2


@pytest.fixture
def fixture_3():
    operation_test_3 = {'date': '2001-11-19T09:22:25.899614',
                        'operationAmount': {'amount': '30153.72',
                                            'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод организации',
                        'from': 'Visa Gold 8326537236216459',
                        'to': 'MasterCard 6783917276771847'}
    return operation_test_3


def test_get_last_five_operations(utils_fixture):
    assert get_last_five_operations(utils_fixture) == [{"id": "1", "date": "07.01.2024", "state": "EXECUTED"},
                                                       {"id": "6", "date": "06.01.2024", "state": "EXECUTED"},
                                                       {"id": "7", "date": "05.01.2024", "state": "EXECUTED"},
                                                       {"id": "5", "date": "04.01.2024", "state": "EXECUTED"},
                                                       {"id": "4", "date": "02.01.2024", "state": "EXECUTED"}]


def test_date(fixture_1):
    assert date(fixture_1) == "08.12.2000"


def test_operation_from_1(fixture_2):
    assert operation_from(fixture_2) == "Maestro 7810 84** **** 5568"


def test_operation_from_2(fixture_3):
    assert operation_from(fixture_3) == "Visa Gold 8326 53** **** 6459"


def test_operation_to_1(fixture_1):
    assert operation_to(fixture_1) == "Счет **5907"


def test_operation_to_2(fixture_3):
    assert operation_to(fixture_3) == "MasterCard **1847"
