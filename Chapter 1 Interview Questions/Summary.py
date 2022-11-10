"""
Summary Test
"""

#1.1
def is_unique(s):
    if len(s) > 128:
        return False

    has_char_array = [False] * 128

    for i in s:
        if has_char_array[ord(i)]:
            return False
        else:
            has_char_array[ord(i)] = True

    return True

print(is_unique("poular"))

#1.2
def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    char_counts = [0] * 128
    
    for i in s1:
        char_counts[ord(i)] += 1

    for i in s2:
        char_counts[ord(i)] -= 1
        if char_counts[ord(i)] < 0:
            return False

    return True

print(check_permutation("God", "doG"))

#1.3
def URLify(s, l):
    space_count = s[0:l].count(" ")
    space_shifts = space_count * 2

    s = [*s]
    for i in range(l - 1, -1, -1):
        if s[i] != " ":
            s[i + space_shifts] = s[i]
        else:
            s[i + space_shifts] = "0"
            s[i + space_shifts - 1] = "2"
            s[i + space_shifts - 2] = "%"
            space_shifts -= 2

    return "".join(s)

print(URLify("Mr  John  Smith        ", 15))

#1.4
def palindrome_permutation(s):
    s = s.lower().replace(" ", "")
    char_counts = [0] * 128

    for i in s:
        char_counts[ord(i)] += 1
    
    count = 0
    for i in char_counts:
        count += i % 2

    return count<=1


print(palindrome_permutation("Tact Coa"))

#1.5
def one_away(s1, s2):

    if len(s1) == len(s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count+=1
                if count > 1:
                    return False
        return True

    else:
        if len(s1) + 1 == len(s2):
            longer_s = s1
            shorter_s = s2
        elif len(s2) + 1 == len(s1):
            longer_s = s2
            shorter_s = s1
        else:
            return False

        index = 0
        count = 0
        for i in range(len(shorter_s)):
            if shorter_s[i] == longer_s[index]:
                index += 1
            else:
                count += 1
                if count > 1:
                    return False
        return True

print(one_away("bake", "pale"))

#1.6
def str_compression(s):
    s_new = []
    count = 0
    for i in range(len(s)):
        count += 1

        if(i == len(s) - 1 or s[i] != s[i+1]):
            s_new.append(str(s[i]))
            s_new.append(str(count))
            count = 0

    if len(s_new) > len(s):
        return s
    else:
        return "".join(s_new)

print(str_compression("abca"))

#1.7
def rotate_matrix(m):
    if len(m) != len(m[0]):
        return False

    for i in range(len(m)):
        for j in range(i, len(m)):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp

    for i in range(len(m)):
        for j in range(len(m)//2):
            temp = m[i][j]
            m[i][j] = m[i][len(m) - j - 1]
            m[i][len(m) - j - 1] = temp

    return m

print(rotate_matrix([[3, 3 ,3], [2, 2, 2], [4, 4, 4]]))


#1.8
def zero_matrix(m):
    row_has_zero = [False] * len(m[0])
    column_has_zero = [False] * len(m[0])

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                row_has_zero[i] = True
                column_has_zero[j] = True

    for i in range(len(row_has_zero)):
        if row_has_zero[i]:
            for j in range(len(m[0])):
                m[i][j] = 0

    for j in range(len(column_has_zero)):
        if column_has_zero[j]:
            for i in range(len(m)):
                m[i][j] = 0

    return m

print(zero_matrix([[3, 0 ,3], [2, 2, 2], [4, 0, 4]]))

#1.9
def str_rotation(s1, s2):
    if(len(s1) == len(s2) and len(s1) > 0):
        return (s1 + s1).__contains__(s2)

    return False

print(str_rotation("waterbottle", "erbottlewat"))




















    
        
            

