# April 3, 2020 - Daily Interview Pro
# Hi, here's your problem today. This problem was recently asked by Microsoft:
# You are given two linked-lists representing two non-negative integers. The
# digits are stored in reverse order and each of their nodes contain a single
# digit. Add the two numbers and return it as a linked list.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        val1 = self.__parse_val_from_list(l1)
        val2 = self.__parse_val_from_list(l2)
        
        sum_val = val1 + val2
        result_list = [ListNode(int(x)) for x in str(sum_val)]
        list_len = len(result_list)
        for i, lnode in enumerate(result_list):
            if i + 1 < list_len:
                result_list[i + 1].next = lnode
        return result_list[-1]
    
    def __parse_val_from_list(self, list_node):
        val = list_node.val
        node = list_node.next
        mult = 10
        while node:
            val += node.val * mult
            mult *= 10
            node = node.next
        return val
    
    def addTwoNumbersDirect(self, l1, l2):
        sum_arr = []
        carry_over = 0
        n1 = l1
        n2 = l2
        while n1:
            current_val = n1.val
            if n2:
                current_val += n2.val
                n2 = n2.next
            n1 = n1.next
            current_val += carry_over
            carry_over = 0
            if current_val >= 10:
                carry_over = 1
            sum_arr.append(current_val % 10)
        while n2:
            current_val = n2.val + carry_over
            n2 = n2.next
            carry_over = 0
            if current_val >= 10:
                carry_over = 1
            sum_arr.append(current_val % 10)
        if carry_over:
            sum_arr.append(carry_over)

        result_list = [ListNode(int(x)) for x in sum_arr]
        list_len = len(result_list)
        for i, lnode in enumerate(result_list):
            if i + 1 < list_len:
                lnode.next = result_list[i + 1]
        return result_list[0]




        

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(7)

    # result = Solution().addTwoNumbers(l1, l2)
    result = Solution().addTwoNumbersDirect(l1, l2)
    while result:
        print(result.val, end=' ')
        result = result.next
        # 7 0 8
