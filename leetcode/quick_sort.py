

def quick_sort(ls):
    if len(ls) == 1:
        return ls

    if len(ls) == 2:
        if ls[0] > ls[1]:
            ls.reverse()
        return ls

    pivot_idx = len(ls)/2 - 1
    pivot_value = ls[pivot_idx]

    # switch pivot and last value
    temp = ls[pivot_idx]
    ls[pivot_idx] = ls[len(ls) - 1]
    ls[len(ls) - 1] = temp

    left_idx = 0
    right_idx = len(ls) - 2
    while left_idx < right_idx:
        if ls[left_idx] < pivot_value and ls[right_idx] < pivot_value:
            left_idx += 1

        if ls[left_idx] > pivot_value and ls[right_idx] > pivot_value:
            right_idx -= 1

        if ls[left_idx] > pivot_value and ls[right_idx] < pivot_value:
            temp = ls[left_idx]
            ls[left_idx] = ls[right_idx]
            ls[right_idx] = temp
            left_idx += 1

        if ls[left_idx] < pivot_value and ls[right_idx] > pivot_value:
            left_idx += 1
    
    if ls[left_idx] > ls[len(ls) - 1]:
        temp = ls[left_idx]
        ls[left_idx] = ls[len(ls) - 1]
        ls[len(ls) - 1] = temp

    # split lists by pivot value
    left_ls = ls[:left_idx + 1]
    right_ls = ls[left_idx + 1:]

    print('{} {}'.format(left_ls, right_ls))

    left_ls = quick_sort(left_ls)
    right_ls = quick_sort(right_ls)

    print('{} {}'.format(left_ls, right_ls))

    return left_ls + right_ls


if __name__ == '__main__':
    import numpy as np
    x = np.arange(21)
    np.random.shuffle(x)
    print(x.tolist())
    quick_sort(x.tolist())
