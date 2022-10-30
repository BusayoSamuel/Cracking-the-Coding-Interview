"""
    One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace 
    a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""
def one_way(s1, s2):
    letter_set = set(s1 + s2)
    return len(letter_set) == len(s1)  or len(letter_set) == len(s2)

print(one_way("pale", "ale"))
