# September 23, 2020 - Daily Interview Pro (done July 19 2021)
# Hi, here's your problem today. This problem was recently asked by Apple:
# Given a string, we want to remove 2 adjacent characters that are the same,
# and repeat the process with the new string until we can no longer perform
# the operation.
# Ex: Start with input = 'cabba'
# After remove 'bb': 'caa'
# After remove 'aa': 'c'
# Output: 'c'
# Input: "banana" => Output: "anana"
# Input: "million" => Output: "illi"

def remove_adjacent_dup(s):
  # Fill this in.
  seen = []
  for letter in s:
    # len(seen) > 0
    if len(seen):
      # if last seen == letter, pop last seen
      if seen[-1] == letter:
        seen.pop()
      else:
        # else add to seen stack
        seen.append(letter)
      # continue
    else:
      # add to seen stack
      seen.append(letter)
      # continue
  # print(seen)
  return ''.join(seen)

print(remove_adjacent_dup('cabba'))
print(remove_adjacent_dup('abcdefghilskajdfh'))
print(remove_adjacent_dup('cabbac'))
print(remove_adjacent_dup('cabbaca'))
print(remove_adjacent_dup('abbaabba'))
