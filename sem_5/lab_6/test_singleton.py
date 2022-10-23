from main import CurrenciesList
import unittest


class Test(unittest.TestCase):
    def test_is_singleton(self):
        my_cur_list = CurrenciesList()
        my_cur_list2 = CurrenciesList()
        self.assertEqual(id(my_cur_list), id(my_cur_list2))


if __name__ == '__main__':
    unittest.main()
