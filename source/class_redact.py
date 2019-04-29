import unittest

def redact(words, banned_words):       # O(n + m)
    if len(banned_words) == 0:
        return words
    banned_words = set(banned_words)
    redacted_arr = []
    for word in words:                  # O(n) n being # of words in words
        if word not in banned_words:    # O(m) m being # of words in banned_words
            redacted_arr.append(word)
    print(redacted_arr)
    return redacted_arr

class SetTest(unittest.TestCase):
    def test_one_word(self):
        words = ['first', 'second', 'badword1', 'third', 'badword2', 'badword1', 'tater']
        banned_words = ['badword1']
        redacted_words = redact(words, banned_words)
        assert banned_words[0] not in redacted_words
    
    def test_two_words(self):
        words = ['first', 'second', 'badword1', 'third', 'badword2', 'tater']
        banned_words = ['badword1', 'badword2']
        redacted_words = redact(words, banned_words)
        assert banned_words[0] not in redacted_words
        assert banned_words[1] not in redacted_words

    def test_multiple_instances(self):
        words = ['first', 'second', 'badword1', 'third', 'badword2', 'badword1', 'tater']
        banned_words = ['badword1', 'badword2']
        redacted_words = redact(words, banned_words)
        assert banned_words[0] not in redacted_words
        assert banned_words[1] not in redacted_words

    def test_empty_banned(self):
        words = ['first', 'second', 'badword1', 'third', 'badword2', 'badword1', 'tater']
        banned_words = []
        redacted_words = redact(words, banned_words)
        assert words == redacted_words
