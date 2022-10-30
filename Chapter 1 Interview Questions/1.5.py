"""
    One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace 
    a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""
def one_way(s1, s2):
    letter_set = set(s1 + s2)
    return len(letter_set) == len(s1)  or len(letter_set) == len(s2)

print(one_way("pale", "ale"))


#Solution 1
def one_way_solution1(first, second):

    def main():
        if len(first) == len(second):
            return one_edit_replace(first, second)
        elif len(first) > len(second):
            return one_edit_insert(second, first)
        else:
            return one_edit_insert(first, second)

    def one_edit_replace(s1, s2):
        found_difference = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if found_difference:
                    return False
                found_difference = True

        return True

    def one_edit_insert(s1, s2):
        index1 = 0
        index2 = 0

        while index1 < len(s1) and index2 < len(s2):
            if s1[index1] != s2[index2]:
                if index1 != index2:
                    return False
                index2 += 1
            else:
                index1 += 1
                index2 += 1

        return True

    return main()

print(one_way_solution1("pale", "ale"))
