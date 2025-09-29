import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# C-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_fibonacci_small():
    """Test Fibonacci arvude arvutamist."""
    assert [fibonacci(i) for i in range(6)] == [0,1,1,2,3,5]
    assert fibonacci(10) == 55

def test_prime_factors_basic():
    """Test algtegurite leidmist."""
    assert prime_factors(12) == [2,2,3]
    assert prime_factors(97) == [97]

#
def test_moving_average_basic():
    """Liikuv keskmise arvutamise test"""
    values = [1, 2, 3, 4, 5]
    assert moving_average(values, 1) == [1, 2, 3, 4, 5]
    assert moving_average(values, 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average(values, 3) == [2.0, 3.0, 4.0]
    assert moving_average(values, 6) == []
    with pytest.raises(ValueError):
        moving_average(values, 0)

def test_normalize_scores_basic():
    """Hindade normaliseerimise test 0 kuni 100"""
    scores = [10, 65, 100]
    normalized = normalize_scores(scores)
    assert normalized == [0.1, 0.65, 1.0]
    with pytest.raises(ValueError):
        normalize_scores([-1, 50, 100])
    with pytest.raises(ValueError):
        normalize_scores([0, 50, 101])


def test_bank_account_creation():
    """Konto loomise test"""
    account = BankAccount("Daria", 100)
    assert account.balance() == 100
    with pytest.raises(ValueError):
        BankAccount("", 50)
    with pytest.raises(ValueError):
        BankAccount("Valeria", -10)

def test_deposit_and_withdraw():
    """Sissemakse ja väljamakse test"""
    account = BankAccount("Daria", 100)
    account.deposit(50)
    assert account.balance() == 150
    with pytest.raises(ValueError):
        account.deposit(0)
    with pytest.raises(ValueError):
        account.deposit(-10)
    
    account.withdraw(70)
    assert account.balance() == 80
    with pytest.raises(ValueError):
        account.withdraw(0)
    with pytest.raises(ValueError):
        account.withdraw(-5)
    with pytest.raises(ValueError):
        account.withdraw(1000) 

def test_transfer_to():
    """Kontode vaheline ülekande test"""
    a1 = BankAccount("Daria", 100)
    a2 = BankAccount("Valeria", 40)
    a1.transfer_to(a2, 50)
    assert a1.balance() == 50 
    assert a2.balance() == 90  
    with pytest.raises(ValueError):
        a1.transfer_to(a2, 0)
    with pytest.raises(ValueError):
        a1.transfer_to(a2, -10)
    with pytest.raises(ValueError):
        a1.transfer_to(a2, 1000)
    with pytest.raises(ValueError):
        a1.transfer_to("not_account", 10)
        


# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!

