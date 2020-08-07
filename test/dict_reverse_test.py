import unittest
import dict_reverse as DictReverseClass


class DictReverseTestCase(unittest.TestCase):

    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_1_dictElementGet(self):
        expected = None
        actual = {}
        result = DictReverseClass.dictElementGet(actual)
        self.assertEqual(expected, result)

    def test_2_dictElementGet(self):
        expected = ['b', 'a']
        actual = {'a': 'b'}
        result = DictReverseClass.dictElementGet(actual)
        self.assertEqual(expected, result)

    def test_3_dictElemntGet(self):
        expected = ['e', 'd', 'c', 'b', 'a']
        actual = {
            'a': {
                'b': {
                    'c': {
                        'd': 'e'
                    }
                }
            }
        }
        result = DictReverseClass.dictElementGet(actual)
        self.assertEqual(expected, result)

    def test_1_get_reverse_dict(self):
        expected = None
        actual = None
        result = DictReverseClass.get_reverse_dict(actual)
        self.assertEqual(expected, result)

    def test_2_get_reverse_dict(self):
        expected = {
            'a': {
                'b': {
                    'c': {
                        'd': 'e'
                    }
                }
            }
        }
        actual = ['a', 'b', 'c', 'd', 'e']
        result = DictReverseClass.get_reverse_dict(actual)
        self.assertEqual(expected, result)


if __name__ == '__main__':

    suite = (unittest.TestLoader().loadTestsFromTestCase(DictReverseTestCase))
    unittest.main(verbosity=2)

