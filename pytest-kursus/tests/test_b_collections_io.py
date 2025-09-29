import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_unique_sorted_basic():
    """Test unikaalsete sorteeritud arvude funktsiooni."""
    assert unique_sorted([3,1,2,2,3]) == [1,2,3]
    assert unique_sorted([]) == []
    assert unique_sorted([5,5,5]) == [5]

def test_count_words_basic():
    """Test sõnade loendamise funktsiooni."""
    text = "tere tere tulemast koju"
    out = count_words(text)
    assert out == {"tere": 2, "tulemast": 1, "koju": 1}

def test_merge_dicts_basic():
    """Kontrollige uue sõnastiku tagastamise funktsiooni."""
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    out = merge_dicts(d1, d2)
    assert out == {"a": 1, "b": 3, "c": 4}
    assert d1 == {"a": 1, "b": 2}

def test_find_max_pair_basic():
    """Funktsiooni kontrollimine tagastamine (max, näitajate_arv); kui tühi, ValueError."""
    nums = [1, 3, 3, 2]
    assert find_max_pair(nums) == (3, 2)

def test_find_max_pair_error():
    """Funktsiooni kontrollimine tühja nimekirja vea suhtes"""
    with pytest.raises(ValueError):
        find_max_pair([])

def test_flatten_basic():
    """Sisestatud loendite lahtivõtmise funktsiooni kontrollimine"""
    nested = [[1, 2, 3], [], [4, 5], [6]]
    assert flatten(nested) == [1, 2, 3, 4, 5, 6]

def test_safe_get_basic():
    """Funktsiooni kontrollimine väärtuse saamiseks võtme järgi"""
    d = {"x": 15}
    assert safe_get(d, "x") == 15
    assert safe_get(d, "y") is None
    assert safe_get(d, "y", default=5) == 5

def test_top_n_basic():
    """Funktsiooni kontrollimine maksimaalse väärtuse valimisel"""
    nums = [1, 6, 5, 3, 2, 4]
    assert top_n(nums, 3) == [6, 5, 4]

def test_chunk_list_basic():
    """Funktsiooni kontrollimine nimekirja jagamiseks"""
    lst = [1, 2, 3, 4, 5, 6, 7]
    assert chunk_list(lst, 2) == [[1, 2], [3, 4], [5, 6], [7]]

def test_chunk_list_error():
    with pytest.raises(ValueError):
        chunk_list([1, 2, 3], 0)

def test_read_write_file_basic(tmp_path):
    """Faili kirjutamise ja lugemise funktsiooni kontrollimine"""
    f = tmp_path / "tekst.txt"
    text = "Hello World!"
    written = write_file(f, text)
    assert written == len(text)
    content = read_file(f)
    assert content == text


# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
