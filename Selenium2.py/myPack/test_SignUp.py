import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to SignUp")
    yield
    print("Closing browser after SignUp")


def test_SignupByemail(setUp):
    print("This is SIgnup By email test")


def test_SignupByfacebook(setUp):
    print("This is signup By facebook test")