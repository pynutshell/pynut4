""" This module tests function reverse_words
provided by module mod.py. """
import unittest
import mod


class ModTest(unittest.TestCase):

    def testNormalCaseWorks(self):
        self.assertEqual(
            mod.reverse_words('four score and seven years'),
            'years seven and score four')

    def testSingleWordIsNoop(self):
        self.assertEqual(
            mod.reverse_words('justoneword'),
            'justoneword')

    def testEmptyWorks(self):
        self.assertEqual(mod.reverse_words(''), '')

    def testRedundantSpacingGetsRemoved(self):
        self.assertEqual(
            mod.reverse_words('with   redundant   spacing'),
            'spacing redundant with')

    def testUnicodeWorks(self):
        self.assertEqual(
            mod.reverse_words('𝒰𝓷𝓲𝓬𝓸𝓭𝓮 is all right too'),
            'too right all is 𝒰𝓷𝓲𝓬𝓸𝓭𝓮')

    def testExactlyOneArgumentIsEnforced(self):
        with self.assertRaises(TypeError):
            mod.reverse_words('one', 'another')

    def testArgumentMustBeString(self):
        with self.assertRaises((AttributeError, TypeError)):
            mod.reverse_words(1)


if __name__ == '__main__':
    unittest.main()
