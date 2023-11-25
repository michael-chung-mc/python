import libstring
import unittest

def CanaryTest_WithDefault_ExpectTrue():
    assert 1 == 1
    assert True

class Test_Anagram(unittest.TestCase):
    def AnagramSortedSolution_WithAnagrams_ExpectTrue(self):
        self.assertEqual(libstring.Anagram.SortedSolution("a","a"),True)
    def AnagramSortedSolution_WithoutAnagrams_ExpectFalse(self):
        self.assertEqual(libstring.Anagram.SortedSolution("ab","a"),False)

if __name__ == '__main__':
    unittest.main()