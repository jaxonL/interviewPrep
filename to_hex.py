"""
Sept 21 2020 - Daily Interview Pro (started July 21 2021, July 25 2021)
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a non-negative integer n, convert the integer to hexadecimal and
return the result as a string. Hexadecimal is a base 16 representation of
a number, where the digits are 0123456789ABCDEF. Do not use any builtin
base conversion functions like hex.
"""

HEX_DIGITS = ['0', '1', '2', '3',
              '4', '5', '6', '7',
              '8', '9', 'A', 'B',
              'C', 'D', 'E', 'F']

def to_hex(n):
  res = ''
  if n < 0:
    print('Please provide a non-negative integer value.')
    return None
  if n < 16:
    return HEX_DIGITS[n]
  # start with remainders and build backwards
  curr = n
  while curr > 0:
    remain = curr % 16
    curr = curr // 16
    res += HEX_DIGITS[remain]
  return res[::-1]

def test_to_hex(value):
  actual = '0x' + to_hex(value)
  print('checking', value, '...')
  if int(actual, 16) != value:
    print('\tFailed: expected', hex(value), '; received ', actual)
  else:
    print('\tPassed (', actual, ').')

test_to_hex(123) # 7B
test_to_hex(161)
test_to_hex(255)
test_to_hex(256)
test_to_hex(257)
test_to_hex(2567)
