#!python
import time

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    index = find_index(text, pattern)
    if index is not None:
        return True
    else:
        return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    start_time = time.time()
    if len(pattern) == 0:
        return False
    for i in range(len(text) - len(pattern) + 1):
        if text[i] == pattern[0]:             # Find if first index in pattern matches in string
            pattern_match = True
            for j in range(1, len(pattern)):  # Check if follow indices match pattern
               if text[i + j] != pattern[j]:  # Does not match pattern
                   pattern_match = False
                   i += 1
                   break
            if pattern_match == True:         # Pattern matches
                return i
    print('runtime was:', (time.time() - start_time))
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    start_time = time.time()
    indices_list = []
    text = list(text)
    i = 0
    offset = 0
    if pattern == '':
        for index in range(len(text)):
            indices_list.append(index)
        return indices_list
    while i < len(text):
        index = find_index(''.join(text), pattern)
        if index is not None:
            if index + offset not in indices_list:
                indices_list.append(index + offset)
            text = text[1:]
            offset += 1
            i = 0
        else:
            i += 1
    print (indices_list)
    print('runtime was:', (time.time() - start_time))
    return indices_list


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))



def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
