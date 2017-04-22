import unittest

from detector2 import check_input_args, generate_tuples


class TestCheckInputArgs(unittest.TestCase):
    def test(self):
        self.assertTrue(check_input_args(3))
        self.assertTrue(check_input_args(4))

    # def test_2(self):
    #     self.assertTrue(check_input_args(2))
    #     self.assertFalse(check_input_args(5))
    #     self.assertFalse(check_input_args(10))



class TestGenerateTuples(unittest.TestCase):
    def test(self):
        test_str = "go for a run"
        N = 3
        expected_result = [['go', 'for', 'a'], ['for', 'a', 'run']]
        self.assertEqual(generate_tuples(test_str, N), expected_result)


if __name__ == "__main__":
    unittest.main()