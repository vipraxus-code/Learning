from utils import Employee
from pytest import fixture

@fixture
def employee():
    return Employee("Mark", "Hank")

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 35000

def test_give_nonstandart_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 40000