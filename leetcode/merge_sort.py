

def merge(ls1, ls2):
    ordered_list = []
    
    i = 0 # counter for ls1
    j = 0 # counter for ls2
    while(i < len(ls1) and j < len(ls2)):
        # adds values in combination list until one of the lists runs out
        if(ls1[i] < ls2[j]):
            ordered_list = ordered_list + [ls1[i]]
            i += 1
        else:
            ordered_list = ordered_list + [ls2[j]]
            j += 1
    
    if(i < len(ls1)):
        leftover = ls1[i:]
    else:
        leftover = ls2[j:]

    # leftover value is already sorted so we can add them together
    return ordered_list + leftover


def merge_sort(ls):
    if len(ls) == 1:
        # stops the recursion at list length 1
        # lists of length 1 are technically sorted
        return ls

    # splitting the list in half
    mid = len(ls)/2
    array_one = ls[:mid]
    array_two = ls[mid:]

    # recursive step to further break down the lists in half until it reaches a list of length 1
    array_one = merge_sort(array_one)
    array_two = merge_sort(array_two)

    # returns the merged list up one level
    return merge(array_one, array_two)


if __name__ == '__main__':
    import numpy as np
    x = np.arange(21)
    np.random.shuffle(x)
    print(x.tolist())
    print(merge_sort(x.tolist()))
