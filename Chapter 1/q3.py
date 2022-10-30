"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient
space at the end to hold the additional characters, and that you are given the 'true' length of the string

EXAMPLE
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20%Smith"
"""
def URLify(s):
	s = [*s]

	for i,v in enumerate(s):
		if v == " ":
			k = len(s) - 1
			while k > i:
			    s[k] = s[k-2]
			    k -= 1
			    print(s)
			
			s[i] = "%"
			s[i+1] = "2"
			s[i+2] = "0"
			i += 2

	new_s = ""
	for i in s:	
		new_s = new_s + i

	return new_s, s

print(URLify("Mr John Smith    "))

def URLify_answer(s, l):
	#s = [*s]
	
	number_of_spaces = s[0:13].count(" ")
	newIndex = l - 1 + (number_of_spaces * 2)
	
	
	if newIndex + 1 < len(s):
		s[newIndex + 1] = "\0"

	oldIndex = l - 1
	while oldIndex >= 0:
		if s[oldIndex] == " ":
			s[newIndex] = "0"
			s[newIndex-1] = "2"
			s[newIndex-2] = "%"
			newIndex -= 3
		else:
			s[newIndex] = s[oldIndex]
			newIndex -= 1
		
		oldIndex -= 1

	return "".join(s)
    
print(URLify_answer(['M', 'r', ' ','J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' ', ' ', ' '], 13))
print('\0')
