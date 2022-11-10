"""
 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1
 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of
 "erbottlewat")
"""
def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    index = None

    for i in range(len(s1)):
        if s1.__contains__(s2[i:]):
            index = i
            break

    if index != None:
        if s1 == (s2[index:] + s2[:index]):
            return True
    
    return False

  

print(string_rotation("waterbottle", "erbottlewat"))
print(string_rotation("beed", "eeda"))
print(string_rotation("bbeed", "beedb"))

def string_rotation_solution(s1, s2):
    s1_len = len(s1)

    if s1_len == len(s2) and s1_len > 0:
        return (s1 + s1).__contains__(s2)
    
    return False

print(string_rotation_solution("waterbottle", "erbottlewat"))
print(string_rotation_solution("beed", "eeda"))
print(string_rotation_solution("bbeed", "beedb"))


