


def permutate(word):
    permutations = []

    word_list = [ch for ch in word]
    word_length = len(word)
    
    def permutate_recurse(x, leftover):
        if len(leftover) == 0:
            return x

        for i in range(0, len(leftover)):
            x_temp = x
            leftover_temp = list(leftover)
            char = leftover[i]
            del leftover_temp[i]
            
            if len(x_temp + char) == word_length:
            	permutations.append(x_temp + char)

            permutate_recurse(x_temp + char, leftover_temp)

    permutate_recurse('', word_list)
    return permutations

print permutate('abc')