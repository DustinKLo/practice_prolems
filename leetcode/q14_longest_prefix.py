
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    common_prefix = ''
    letter_index = 0
    while True:
    	letter_set = list(set([word[letter_index:letter_index+1] for word in strs]))
    	if len(letter_set) == 1:
    		if len(letter_set[0]) == 0:
    			break
    		common_prefix += letter_set[0][0]
    	
    	else:
    		break

    	letter_index += 1

    return ''.join(common_prefix)



if __name__ == '__main__':
	w = ["flower","flow","flight"]
	print(longestCommonPrefix(w))
	print(longestCommonPrefix(['']))
