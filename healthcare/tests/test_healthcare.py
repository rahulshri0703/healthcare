from healthcare import __version__
from healthcare import bmi


def test_version():
    assert __version__ == '0.1.0'


def test_bmi():
    result = bmi(54, 1.7)
    assert result == 18
