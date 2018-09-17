
def quick_sort(ls):
    if len(ls) <= 1:
        return ls

    if len(ls) == 2:
        if ls[0] > ls[1]:
            ls.reverse()
        return ls

    print ls

    pivot_idx = len(ls)/2 #- 1
    pivot_value = ls[pivot_idx]
    
    left_ls = filter(lambda x: x < pivot_value, ls)
    left_ls.append(pivot_value)
    right_ls = filter(lambda x: x > pivot_value, ls)

    print '{} {}'.format(left_ls, right_ls)

    left_ls = quick_sort(left_ls)
    right_ls = quick_sort(right_ls)

    print '{} {}'.format(left_ls, right_ls)

    return left_ls + right_ls
    

if __name__ == '__main__':
    import numpy as np
    x = np.arange(21)
    np.random.shuffle(x)
    print x.tolist()
    quick_sort(x.tolist())