"""
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is 
    the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
    You can ignore casing and non-letter characters
    EXAMPLE
    Input: Tact Coa
    Output: True(permuatations: "taco cat", "atco cta", etc.)
"""
import itertools 
import collections

def is_palindrome_permutation(s):
    permutation_list = list(itertools.permutations(s))  #Returns a list of tuples
    
    for i in range(len(permutation_list)):  #Never do len() - 1
        permutation_list[i] = "".join(permutation_list[i])

    for i in permutation_list:
        if permutation_list.count(i[::-1]) > 0:  #sorted() only works in ascending or descending order or with a function
            return True 

    return False

print(is_palindrome_permutation("Tact Coa"))

#Solution 1
def is_palindrome_permutation_solution_1(s):
    def get_char(c):
        a = ord('a')
        z = ord('z')
        val = ord(c)

        if val >= a and val <= z:
            return val - a
        else:
            return -1
        
    def getCharFrequencyTable(s):
        table = [0] * (ord('z') - ord('a') + 1)

        for i in s:
            x = get_char(i)
            if x != -1:
                table[x] += 1

        return table

    char_count = getCharFrequencyTable(s)
    
    print(char_count)

    found_odd = False

    for i in char_count:
        if i % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    
    return True


print(is_palindrome_permutation_solution_1("tact coa")) #"You can ignore casing and non-letter characters"

#Solution 2
def is_palindrome_permutation_solution_2(s):
    def get_char(c):
        a = ord('a')
        z = ord('z')
        val = ord(c)

        if val >= a and val <= z:
            return val - a
        else:
            return -1
        
    count_Odd = 0
    table = [0] * (ord('z') - ord('a') + 1)

    for i in s:
        x = get_char(i)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                count_Odd += 1
         #  else:
         #      count_Odd -= 1
         #Probably not needed

    return count_Odd >= 1


print(is_palindrome_permutation_solution_2("tact coka")) #"You can ignore casing and non-letter characters"
