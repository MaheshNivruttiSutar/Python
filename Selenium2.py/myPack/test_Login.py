#Multiple way to Run Test Cases:
'''
py.test_mod.py    (run tests in module)
py.test somepath  (run all tests below somepath
py.test_module.py::test_method   (only run test_method in test_module)

-s to print statements
-v verbose
'''
#COMMANDS:
'''
-Run all tests in a module/file:
pytest-v-s test_Login.py
pytest-v-s test_SignUp.py

-Run all test(from all modules) in a path
pytest-v-s C:\Users\admin\PycharmProjects\Selenium2\myPack\

-Run specific test method from a module:
pytest -v-s test_Login.py::test_loginbyfacebook '''


import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to Login")
    yield
    print("Closing browser after Login")


def test_loginByemail(setUp):
    print("This is login By email test")


def test_loginByfacebook(setUp):
    print("This is login By facebook test")