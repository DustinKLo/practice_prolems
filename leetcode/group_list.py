

x = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e', 'f']
[['a', 'a', 'a', 'a'], ['b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']]
[['a', 'a', 'a', 'a'], ['b'], ['c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']]
[['a', 'a', 'a', 'a'], ['b'], ['c', 'c'], ['a', 'a', 'd', 'e', 'e', 'e', 'e']]
[['a', 'a', 'a', 'a'], ['b'], ['c', 'c'], ['a', 'a'], ['d', 'e', 'e', 'e', 'e']]
[['a', 'a', 'a', 'a'], ['b'], ['c', 'c'], ['a', 'a'], ['d'], ['e', 'e', 'e', 'e']]


def group_list(ls):
    if ls == []:
        return ls
    
    main_letter = ls[0]
    index = 1
    for i in range(1, len(ls)):
        if ls[i] == main_letter:
            index += 1
        else:
            break

    sublist = ls[0:index]
    tail = ls[index:]
    print [sublist] + tail
    return [sublist] + group_list(tail)

print x
print '\n'
print group_list(x)



def flatten(x):
	if x == []:
		return x
	if isinstance(x[0], list):
		return flatten(x[0] + x[1:])
	return [x[0]] + flatten(x[1:])


t = [ 1, 2, 3, [1,2,3], 4, 5, 6, [7, [8, 9]], 10, [11] ]
print t
print '\n'
print flatten(t)


def dropN(n, ls):
	if len(ls) < n:
		return ls

	head_n = ls[0:n-1]
	tail = ls[n:]
	return head_n + dropN(n, tail)

print dropN(3, [1,2,3,4,5,6,7,8,9,10])
print dropN(4, [1,2,3,4,5,6,7,8,9,10])
print dropN(5, [1,2,3,4,5,6,7,8,9,10])
print dropN(5, [1,2,3,4,5,6])



from itertools import combinations
def get_all_combinations(n, ls):
	# if n == len(ls):
	# 	return ls

	return list(combinations(ls, n))

get_all_combinations(3, [1,2,3,4,5,6])


