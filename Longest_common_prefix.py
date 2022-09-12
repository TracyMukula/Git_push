def longestCommonPrefix( p):
	size = len(p)
# if size is 0, return empty string
	if (size == 0):
		return ""

	if (size == 1):
		return p[0]
# sort 
	p.sort()
	
# find the minimum length of the first and last string using indexing
	length = min(len(p[0]), len(p[-1]))

# finding the common prefix
	i = 0
	while (i < length and p[0][i] == p[size - 1][i]): #review?
		i += 1

	pre = p[0][0: i]
	return pre

if __name__ == "__main__":
	input = ["flower", "axe", "floght"]
	# print(input.sort()) #readmore
	print("The longest Common Prefix is :" , longestCommonPrefix(input))

