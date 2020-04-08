# April 7, 2020 - Daily Interview Pro
# Hi, here's your problem today. This problem was recently asked by AirBNB:
# Given a sorted array, A, with possibly duplicated elements, find the
# indices of the first and last occurrences of a target element, x.
# Return-1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]

# best solution is to use binary search and expand on both sides
# worst case is always O(n), in both cases
# avg case would be O(log n) for bin search solution
class Solution: 
    def getRange(self, arr, target):
        s_ind = -1
        e_ind = -1
        # tot_len = len(arr)
        for i, num in enumerate(arr):
            # sorted, so only first index will set s_ind
            if num == target and s_ind == -1:
                s_ind = i
            elif num == target:
                # updates n times -- can i reduce that?
                # probably, but is it worth it? since it's at most n
                e_ind = i
        return [s_ind, e_ind]
  
# Test program 
arrs = [[1, 2, 2, 2, 2, 3, 4, 7, 8, 8], [1,3,3,5,7,8,9,9,9,15], [100, 150, 150, 153], [1,2,3,4,5,6,10]]
xs = [2, 9, 150, 9]
expected = [[1, 4], [6, 8], [1, 2], [-1, -1]]

for i, arr in enumerate(arrs):
    soln = Solution().getRange(arr, xs[i])
    print(f'{i}: {soln} ({soln == expected[i]})')
    # [1, 4]
