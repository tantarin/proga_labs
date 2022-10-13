from main import Bank


def test_invalid_id():
    bank = Bank()
    assert bank.get_valute('R99999') == {'R99999', None}

def test_valid_id():
    bank = Bank()
    assert bank.get_name('R01010') == 'Австралийский доллар'


if __name__ == "__main__":
    test_invalid_id()
    test_valid_id()
    print("Everything passed")
