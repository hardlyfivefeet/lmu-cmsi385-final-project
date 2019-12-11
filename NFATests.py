import sys
import unittest
import NFASimulator

class NFATests(unittest.TestCase):

    def test_even_ones_pass(self):
        with open('test_machines/odd_number_ones.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', '0011']
            result = NFASimulator.simulate_machine()
            self.assertTrue(result)

    def test_even_ones_fail(self):
        with open('test_machines/odd_number_ones.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', '10011']
            result = NFASimulator.simulate_machine()
            self.assertFalse(result)

    def test_even_ones_without_ones(self):
        with open('test_machines/odd_number_ones.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', '000000']
            result = NFASimulator.simulate_machine()
            self.assertTrue(result)

    def test_even_ones_without_zeroes_pass(self):
        with open('test_machines/odd_number_ones.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', '111111']
            result = NFASimulator.simulate_machine()
            self.assertTrue(result)

    def test_even_ones_without_zeroes_fail(self):
        with open('test_machines/odd_number_ones.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', '11111']
            result = NFASimulator.simulate_machine()
            self.assertFalse(result)

    def test_even_ones_with_empty_string(self):
        with open('test_machines/odd_number_ones.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', '']
            result = NFASimulator.simulate_machine()
            self.assertTrue(result)

    def test_only_accept_empty_pass(self):
        with open('test_machines/only_accept_empty.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', '']
            result = NFASimulator.simulate_machine()
            self.assertTrue(result)

    def test_only_accept_empty_fail(self):
        with open('test_machines/only_accept_empty.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', '123121']
            result = NFASimulator.simulate_machine()
            self.assertFalse(result)

    def test_lambda_moves_pass(self):
        with open('test_machines/machine_with_lambda.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', 'aab']
            result = NFASimulator.simulate_machine()
            self.assertTrue(result)

    def test_lambda_moves_fail(self):
        with open('test_machines/machine_with_lambda.txt', 'r') as test_file:
            sys.stdin = test_file
            sys.argv = ['', 'ba']
            result = NFASimulator.simulate_machine()
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
