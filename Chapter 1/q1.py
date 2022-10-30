"""
 Implement an algorithm to determine if a string has all unique characters. What if you 
can not use additional data structures?
"""

def all_unique(s):
    new_s = set()
    for i in s:
        new_s.add(i)
    return len(new_s) == len(s)

print(all_unique("busayo"))

def all_unique_v2(s):
    new_s = []
    for i in s:
        if i not in new_s:
            new_s.append(i)
    return len(new_s) == len(s)

print(all_unique_v2("busayo"))

def all_unique_v3(s):
    new_s = []
    for i in s:
        if i not in new_s:
            new_s.append(i)
        else:
            return False
    return True

print(all_unique_v3("busayo"))

def all_unique_answer(s):
    if len(s) > 128:
        return False

    char_set = [False] * 128

    for i in s:
        if char_set[ord(i)]:
            return False
        else:
            char_set[ord(i)] = True

    return True

print(all_unique_answer("busayo"))
