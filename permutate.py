
def permutate(word):
    permutations = [] # main list to return

    word_list = [ch for ch in str(word)] # separating all letters in word to a list
    word_length = len(str(word))
    
    def permutate_recurse(x, leftover):
        if len(leftover) == 0: # end the recursion
            return x

        for i in range(0, len(leftover)):
            char = leftover[i]
            perm_val = x + char # create one permutation

            leftover_temp = list(leftover) # copying the list of letters
            del leftover_temp[i] # removing the letter from the list becuase it had already been used
            
            if len(perm_val) == word_length: # only add permutation if length matches
                permutations.append(perm_val)

            # RECURSIVE STEP
            # do the step over again with all the permutations for current step
            # and without the letter already used
            permutate_recurse(perm_val, leftover_temp)

    permutate_recurse('', word_list)
    return permutations

print permutate('abcde')
