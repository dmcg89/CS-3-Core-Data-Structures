#!python

from strings import contains, find_index, find_all_indexes
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern
        # Write more positive test cases with assert is True statements
        assert contains('aba', 'b') is True
        assert contains('aac', 'ac') is True

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last
        #  Write more negative test cases with assert is False statements
        assert contains('bananas', 'nnas') is False

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix
        # Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert contains('banananananananaannas', 'anna') is True

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern
        #  Write more positive test cases with assert equal int statements
        assert find_index('abba', 'bb') == 1
        assert find_index('abccbccc', 'ccc') == 5

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is None statements
        assert find_index('abcdef', 'abdeg') is None

    def test_find_index_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_index('ababc', 'abc') == 2  # overlapping prefix
        assert find_index('bananas', 'nas') == 4  # overlapping prefix
        assert find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert find_index('abra cadabra', 'adab') == 6  # overlapping prefix
        #  Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert find_index('alla', 'la') == 2
        assert find_index('rraraceraced', 'raced') == 7

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indexes('abc', 'bc') == [1]
        assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern
        # Write more positive test cases with assert equal list statements
        assert find_all_indexes('abab', 'a') == [0, 2]
        assert find_all_indexes('abcabcabc', 'a') == [0, 3, 6]
        assert find_all_indexes('zasdfsadfaz', 'z') == [0, 10]

    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last
        # Write more negative test cases with assert equal list statements
        assert find_all_indexes('abzazcaba', 'abc') == []
        assert find_all_indexes('abceabedacfd', 'abcd') == []
        assert find_all_indexes('rat', 'tar') == []

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix
        #  Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert find_all_indexes('abcdefabcdef', 'abcdef') == [0, 6]
        assert find_all_indexes('manpigman', 'man') == [0, 6]
        assert find_all_indexes('fatfarfart', 'fa') == [0, 3, 6]


if __name__ == '__main__':
    unittest.main()
