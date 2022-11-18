import unittest
from account import *


class MyTestCase(unittest.TestCase):
    def test_init(self):
        self.assertEqual(self.account_name(), 'John Smith')
        self.assertEqual(self.account_balance(), 500)

    def test_deposit(self):
        self.assertEqual(deposit(500), 1000)

    def test_withdraw(self):
        self.assertEqual(withdraw(200), 800)


if __name__ == '__main__':
    unittest.main()
