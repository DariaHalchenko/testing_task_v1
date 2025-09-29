import math
import pytest
from src.a_basics import (
    add, sub, mul, div, sum_list, is_even, factorial, reverse_string,
    is_palindrome, to_title_case, clamp, median, unique_letters, safe_int, nth_root
)

# A-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_add_basic():
    """Test liitmise funktsiooni."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_sub_basic():
    """Test lahutamise funktsiooni."""
    assert sub(10, 7) == 3
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5

def test_mul_basic():
    """Test korrutamise funktsiooni."""
    assert mul(2, 2) == 4
    assert mul(5, 3) == 15
    assert mul(3, 3) == 9

def test_div_basic():
    """Test korrutamise funktsiooni."""
    assert div(2, 2) == 1
    assert div(15, 3) == 5
    assert div(3, 3) == 1

def test_sum_list_basic():
    """Loendi summa funktsiooni kontrollimine."""
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([3, 5, 5]) == 13
    assert sum_list([-1, -2, 3]) == 0

def test_is_even_basic():
    """Funktsiooni kontrollimine, kui n on paarisarv Tagastab True, muul juhul False."""
    assert is_even(2) is True
    assert is_even(0) is True
    assert is_even(3) is False
    assert is_even(-4) is True
    assert is_even(7) is False

def test_reverse_string_basic():
    "Pöördunud silbi tagastamise kontrollimine"
    assert reverse_string("abc") == "cba"
    assert reverse_string("bvf") == "fvb"
    assert reverse_string("ab") == "ba"
    assert reverse_string("bhjrt") == "trjhb"

def test_to_title_case_basic():
    """Funktsiooni kontrollimine, mis tagastab sõna, kus iga sõna algab suure tähega."""
    assert to_title_case("hello world") == "Hello World"
    assert to_title_case("HELLO world") == "Hello World"
    assert to_title_case("123 abc") == "123 Abc"
    assert to_title_case("bbbCCC 333") == "Bbbccc 333"

def test_clamp_basic():
    """Test clamp funktsiooni."""
    assert clamp(5, 1, 10) == 5
    assert clamp(-5, 0, 10) == 0
    assert clamp(15, 0, 10) == 10
    assert clamp(-6, 3, 8) == 3

def test_unique_letters_basic():
    """Test unique_letters funktsiooni."""
    assert unique_letters("aAabc!") == {"a", "b", "c"}
    assert unique_letters("543") == set()

def test_safe_int_basic():
    """Test safe_int funktsiooni."""
    assert safe_int("123") == 123
    assert safe_int("abc", default=0) == 0
    assert safe_int("12.3", default=-1) == -1
    assert safe_int("456") == 456
    assert safe_int("15.5", default=-1) == -1

def test_factorial_basic():
    assert factorial(0) == 1  
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-3)

def test_is_palindrome_basic():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("Python") is False

def test_median_basic():
    assert median([1, 2, 3]) == 2
    assert median([1, 3, 2, 4]) == 2.5
    assert median([10]) == 10
    with pytest.raises(ValueError):
        median([])

def test_nth_root_basic():
    assert nth_root(27, 3) == 3
    assert nth_root(16, 4) == 2
    with pytest.raises(ValueError):
        nth_root(-16, 2)
    with pytest.raises(ValueError):
        nth_root(16, 0)
    with pytest.raises(ValueError):
        nth_root(16, -2)
    assert nth_root(81, 4) == 3

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
