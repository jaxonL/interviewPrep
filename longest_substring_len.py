# April 4, 2020 - Daily Interview Pro
# Hi, here's your problem today. This problem was recently asked by Microsoft:
# Given a string, find the length of the longest substring
# *without* repeating characters.
# Can you find a solution in linear time?

# Another early stop is to check if the current
# maxLen > the rest of the characters to check. If yes,
# return that
class Solution:
  def lengthOfLongestSubstring(self, s):
    # cannot just assign to {}, cause it assums it's a dict
    seenChar = set()
    maxLongest = len({x for x in s})
    maxLen = 1

    # for i, chara in enumerate(s):
    for chara in s:
        if chara in seenChar:
            # print(i, seenChar, chara, maxLen, len(seenChar))
            currLen = len(seenChar)
            seenChar = set()
            if maxLen < currLen:
                maxLen = currLen
                # early stop
                if maxLen == maxLongest:
                    # cannot be longer than this because
                    # maxLongest is the size of the alphabet
                    return maxLen
        seenChar.add(chara)

    return maxLen

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
    # 10
    print(Solution().lengthOfLongestSubstring('aabbccddeeffgghhiijjkkll'))
    # 2
