
def permutate(word):
    permutations = []

    word_list = [ch for ch in word]
    word_length = len(word)
    
    def permutate_recurse(x, leftover):
        if len(leftover) == 0:
            return x

        for i in range(0, len(leftover)):
            char = leftover[i]
            perm_val = x + char

            leftover_temp = list(leftover)
            del leftover_temp[i]
            
            if len(perm_val) == word_length:
                permutations.append(perm_val)

            permutate_recurse(perm_val, leftover_temp)

    permutate_recurse('', word_list)
    return permutations

print permutate('abcde')
