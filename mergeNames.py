"""
Given two lists A, B, with n, m elements respectively, iterate through a merged list C
(by appending B to A) and keep track of names that have already appeared with a set S.
S acts as a precondition to see if an element e, taken from C, is already in the final
list F. If e is not in S, add e to S and append e to F. If e is in S, continue to the
next element in C. Since existence checking can be done in O(1) time, this takes
O(m + n) time, because we check for each element (m + n elements), which is more
efficient than solution 1.
"""

def merge_names(list_a, list_b):
    all_names = list_a.copy()
    all_names.extend(list_b)
    seen_names = set()
    result = []
    for name in all_names:
        if name not in seen_names:
            result.append(name)
            seen_names.add(name)
    return result

print(merge_names(['Allison', 'Brian', 'Peter'], ['Jason', 'Peter', 'Sara']))
print(merge_names(['Allison', 'Brian', 'Brian', 'Sara'], ['Jason', 'Peter', 'Sara']))
