
def quick_sort(ls):
    if len(ls) <= 1: # stops recursion
        return ls

    if len(ls) == 2: # stops recursion, but also sorts it because sorting list of length 2 is easy
        if ls[0] > ls[1]:
            ls.reverse()
        return ls

    print ls

    pivot_idx = len(ls)/2
    pivot_value = ls[pivot_idx] # choosing pivot value at middle of list
    
    left_ls = filter(lambda x: x < pivot_value, ls) # all values less than pivot are to the left
    left_ls.append(pivot_value) # keep the pivot value at the end
    right_ls = filter(lambda x: x > pivot_value, ls) # all values greater than pivot are to the right

    print '{} {}'.format(left_ls, right_ls)

    # recursive step
    # list less than pivot goes through the same step until it reaches a list of length 1 or 2 (easy to sort)
    left_ls = quick_sort(left_ls)
    # list greater than pivot goes through the same step
    right_ls = quick_sort(right_ls)

    print '{} {}'.format(left_ls, right_ls)

    # once both lists and sorted we can combine them to create a larger sorted list
    return left_ls + right_ls
    

if __name__ == '__main__':
    import numpy as np
    x = np.arange(21)
    np.random.shuffle(x)
    print x.tolist()
    print quick_sort(x.tolist())
