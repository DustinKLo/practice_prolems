

def combination(ls, k):
    ls = [str(i) for i in ls]

    if k == 1: # k is the length of each combination
        return ls
    if k >= len(ls):
        return [''.join(ls)]

    combinations = [] # master list of combinations that function will return

    def combination_recurse(ls, word):
        if len(ls) == 0:
            return None

        # word is the letter of the previous node
        # ls is the list of the rest of the letters
        for i in range(0, len(ls)):
            head, tail = ls[i], ls[i+1:]
            new_word = word + head # create a new word (ie. node)

            if len(new_word) < k: # if the word length shorter than specified, recurse
                print 'branches: {} {}'.format(new_word, tail)
                combination_recurse(tail, new_word)
            else: # if word length is as specified, add it to master list
                print 'end nodes: {} {}'.format(new_word, tail)
                combinations.append(new_word)


    for i in range(0, len(ls)):
    	# creating the root tree nodes
        head, tail = ls[i], ls[i+1:] # head is the first letter of list, tail is the rest
        if len(tail) >= k - 1:
            print 'root tree nodes: {} {}'.format(head, tail)
            combination_recurse(tail, head) # start the recursion

    return combinations


if __name__ == '__main__':
    x = list(range(1,6))
    print combination(x, 3)

