"""
author: Rafal Miecznik
contact: ravmiecznk@gmail.com
"""
from circ_buffer import Cbuffer
import pytest

@pytest.fixture(scope='function')
def cbuffer():
    return Cbuffer()

@pytest.fixture(scope='function')
def cbuffer_size10():
    return Cbuffer(b_size=10)

def test_circ_buffer_default_size(cbuffer):
    """Test if init buffer size == 100"""
    assert cbuffer.size == 100

def test_putchar(cbuffer):
    """Test if put and get char are the same"""
    char = 'a'
    cbuffer.put(char)
    assert cbuffer.get() == char

def test_puts(cbuffer):
    "Test if get string is equal to put string"
    string = "rafal"
    cbuffer.puts(string)
    assert cbuffer.gets() == string
    try:
        cbuffer.puts()
    except TypeError:
        pass

def test_put_combination(cbuffer):
    """Tests combination of put, puts, get, gets"""
    test_strings = ["rafal", "miecznik", "a", "b"]
    for s in test_strings:
        if len(s) > 1:
            cbuffer.puts(s)
        elif len(s) == 1:
            cbuffer.put(s)
    assert cbuffer.gets() == "".join(test_strings)

def test_get_from_empty_buffer(cbuffer):
    """Test if None will be returned if no data in buffer"""
    assert cbuffer.get() == None
    assert cbuffer.gets() == None

def test_available(cbuffer):
    """Test available() method
    available() of empty buffer
    available() if there is some data
    available() if some data was read
    """
    string = "rafal"
    assert cbuffer.available() == 0

    cbuffer.puts(string)
    assert cbuffer.available() == len(string)
    assert cbuffer.gets() == string
    assert cbuffer.available() == 0

def test_available_with_overflow(cbuffer_size10):
    """Test if vailalbe not exceed buffer size"""
    buff_size = len(cbuffer_size10)
    string = "abcdefghijk"
    assert buff_size == 10
    cbuffer_size10.puts(string)
    assert cbuffer_size10.available() == 10

def test_gets_after_overflow(cbuffer_size10):
    """Test gets after overflow"""
    string = "abcdefghijk"  #string of len 10 + 1
    cbuffer_size10.puts(string)
    assert cbuffer_size10.gets() == string[1:]
    string2 = "abcdefghijklmn"  # string of len 10 + 4
    cbuffer_size10.puts(string2)
    assert cbuffer_size10.gets() == string2[4:]

def test_flush(cbuffer_size10):
    """Tests if flush method works"""
    cbuffer_size10.puts(15*"x")
    assert cbuffer_size10.available() == 10

    cbuffer_size10.flush()
    assert cbuffer_size10.available() == 0
    assert cbuffer_size10.get() == None
    assert cbuffer_size10.gets() == None

def test_add_operator(cbuffer_size10):
    cbuffer_size10 += 'a'
    cbuffer_size10 += 'b'
    cbuffer_size10 = cbuffer_size10 + 'c'
    cbuffer_size10 += "defg"
    assert cbuffer_size10.gets() == 'abcdefg'

def test_cbuffer_with_init_values():
    init_string = "rafal"
    cbuffer = Cbuffer(b_size=50, init_buffer=init_string)
    assert cbuffer.available() == len(init_string)
    assert cbuffer.gets() == init_string
    assert cbuffer.gets() == None

def test_cbuffer_get_as_list_method(cbuffer):
    test_string = "test string"
    cbuffer.puts(test_string)
    assert cbuffer.gets_list() == list(test_string)
    assert cbuffer.gets_list() == None

def test_cbuffer_get_as_list_method_with_specifed_amount(cbuffer):
    test_string = "test string"
    cbuffer.puts(test_string)
    assert cbuffer.gets_list(3) == list(test_string[0:3])

def test_cbuffer_get_as_list_method_with_specifed_amount_get_more_than_available(cbuffer):
    test_string = "test string"
    cbuffer.puts(test_string)
    assert cbuffer.gets_list(len(test_string) + 5) == list(test_string)

def test_iteration(cbuffer):
    test_string = "abcdefghijklm"
    retr_string = ''
    cbuffer.puts(test_string)
    for s in cbuffer:
        retr_string += s
    assert test_string == retr_string

def test_contains(cbuffer):
    test_string = "abcdefghijklm"
    cbuffer.puts(test_string)
    assert "f" in cbuffer
    assert "jkl" in cbuffer
    assert "xyz" not in cbuffer

def test_str(cbuffer):
    string = "test"
    assert cbuffer.puts(string).str() == string


if __name__ == "__main__":
    cbuffer = Cbuffer()
    test_string = "abcdefghijklm"
    retr_string = ''
    cbuffer.puts(test_string)
    for s in cbuffer:
        retr_string += s
    assert test_string == retr_string


