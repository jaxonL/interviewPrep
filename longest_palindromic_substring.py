# April 5, 2020 - Daily Interview Pro
# Hi, here's your problem today. This problem was recently asked by Twitter:
# A palindrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.
# Input: "banana" => Output: "anana"
# Input: "million" => Output: "illi"

class Solution: 
    def longestPalindrome(self, s):
        max_len = 0
        max_substr = ''
        num_comps = 0
        tot_len = len(s)
        for start_ind, chara in enumerate(s):
            if tot_len - start_ind < max_len:
                # cannot have longer palindrome; early break
                break
            for end_ind in range(tot_len - 1, start_ind - 1, -1):
                num_comps += 1
                if end_ind + 1 - start_ind < max_len:
                    # cannot have longer palindrome; early break
                    break
                # reverse loop
                if s[end_ind] == chara:
                    if self.__is_palindrome(s[start_ind:end_ind + 1]):
                        # must be max palin starting at ind start
                        curr_palin = s[start_ind:end_ind + 1]
                        # print(curr_palin, len(curr_palin), max_len)
                        if len(curr_palin) > max_len:
                            max_substr = curr_palin
                            max_len = len(curr_palin)
                        break
        print(f'result: {max_substr} (after {num_comps} comps)')
        return max_substr


    def __is_palindrome(self, s):
        # print(f'is "{s}" the same as "{s[::-1]}"? {s== s[::-1]}')
        return s == s[::-1]

if __name__ == '__main__':
    # Test program
    s = "tracecars"
    print(Solution().longestPalindrome(s))
    # racecar
    print(Solution().longestPalindrome('a'))
    # a
    print(Solution().longestPalindrome('million'))
    # illi
    print(Solution().longestPalindrome('jkjkkj'))
    # jkkj
