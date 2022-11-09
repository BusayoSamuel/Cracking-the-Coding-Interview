"""
String Comprehension: Implement a method to basic string compression using the counts of repeated characters. For example, the
string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your 
method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z)
"""

def s_compress(s):
    s = s.lower()
    output = []

    i = 0 #Whenever you use a while loop you have to initialise the variable first
    while i in range(len(s)):
        count = 0
        output.append(s[i])
        print(i)
        while s[i] == output[-1]:
            count += 1
            i += 1
            if i >= len(s):
                break
        output.append(str(count))

    if len(output) < len(s):
        return "".join(output)
    else:
        return s

print(s_compress("aabcccccaaa"))


def s_compress_solution1(s):
    s = s.lower()
    output = []
    count = 0

    for i in range(len(s)):
        count += 1

        if i + 1 >= len(s) or s[i] != s[i+1]:
            output.append(s[i])
            output.append(str(count))
            count = 0
    

    if len(output) < len(s):
        return "".join(output)
    else:
        return s

print(s_compress_solution1("aabcccccaaa"))


