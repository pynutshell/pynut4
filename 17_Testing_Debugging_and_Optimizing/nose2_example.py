# run in the current directory using "nose2 nose2_example.TestCase"

import unittest
from nose2.tools import params


class TestCase(unittest.TestCase):

    @params((5, 5),
            (-1, 1),
            ('a', None, TypeError))
    def test_abs_value(self, x, expected, should_raise=None):
        if should_raise is not None:
            with self.assertRaises(should_raise):
                abs(x)
        else:
            assert abs(x) == expected
