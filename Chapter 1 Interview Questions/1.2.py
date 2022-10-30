"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
"""

def check_permutation(s1, s2):
	if len(s1) != len(s2):
		return False
	
	for i in s1:
		if i not in s2:
			return False
	
	return True


print(check_permutation("gad", "dog"))

def check_permutation_answer(s1, s2):
	s1 = sorted(s1)
	s2 = sorted(s2)
	
	return s1 == s2
    
print(check_permutation_answer("God", "dog"))

#If it wasn't case sensitive
def check_permutation_answer_v2(s1, s2):
	s1 = sorted(s1.lower())
	s2 = sorted(s2.lower())
	
	return s1 == s2
    
print(check_permutation_answer_v2("God", "dog"))

def check_permutation_answer_v3(s1, s2):
	if len(s1) != len(s2):
		return False

	chars = [0] * 128
	for i in s1:
		chars[ord(i)] += 1

	for i in s2:
		chars[ord(i)] -= 1
		if chars[ord(i)] < 0:
			return False

	return True
print(check_permutation_answer_v3("god", "dog"))



