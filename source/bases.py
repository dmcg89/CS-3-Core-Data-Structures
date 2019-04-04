#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Decode digits from binary (base 2)
    digits = list(digits) # Turn string of digits into list of individual
    power = len(digits) - 1
    base_ten_int = 0

    # Decode digits from any base (2 up to 36)
    for digit in digits:
        if digit in string.ascii_letters:       # checks if digit is letter or int
            lower_case = digit.lower()
            hex_value = ord(lower_case) - 87    # converts letter to unicode value
                                                # and subtracts 87 for desired value
            base_ten_int += hex_value * base ** power
            power -= 1
        else:
            int_digit = int(digit)
            base_ten_int += int_digit * base ** power
            power -= 1
    return base_ten_int



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    base_rep = ''
    while number > 0:
        remainder = number % base
        number = number // base
        if remainder > 9:                           # uses letter representation if
                                                    # remainder > 9
            base_rep += str(chr(remainder + 87))    # adds 87 to convert to unicode value
        else:
            base_rep += str(remainder)
    return base_rep[::-1]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    if base1 == base2:
        return digits
    

    num = decode(digits, base1)
    basenew = encode(num, base2)
    return basenew

# print(convert(10, 10, 16))
# print(decode('4B5', 16))
# print(encode(12313, 2))
#
# def main():
#     """Read command-line arguments and convert given digits between bases."""
#     import sys
#     args = sys.argv[1:]  # Ignore script file name
#     if len(args) == 3:
#         digits = args[0]
#         base1 = int(args[1])
#         base2 = int(args[2])
#         # Convert given digits between bases
#         result = convert(digits, base1, base2)
#         print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
#     else:
#         print('Usage: {} digits base1 base2'.format(sys.argv[0]))
#         print('Converts digits from base1 to base2')
#
#
# if __name__ == '__main__':
#     main()
