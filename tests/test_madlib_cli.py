import pytest
from madlib_cli import __version__
from madlib_cli.madlib_cli import *


def test_version():
    assert __version__ == '0.1.0'

def test_read_template_returns_stripped_string():
    actual = reading_file("madlib_cli/tt_file.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# def test_read_not_found():
#     actual = reading_file("madlib_li/tt_file.txt")
#     expected = '404 file not found'
#     assert actual == expected

def test_filter():
    actual = filter_template("It was a {Adjective} and {Adjective} {Noun}.")
    expected = ['Adjective', 'Adjective', 'Noun']
    assert actual == expected

def test_merg():
    actual = merge("It was a {Adjective} and {Adjective} {Noun}.", ['Omar', 'mohammad', 'alzoubi'])
    expected = 'It was a Omar and mohammad alzoubi.'
    assert actual == expected
