

def merge(ls1, ls2):
	# print("\nlist inputs to merge: {} {}".format(ls1, ls2))
	ordered_list = []
	
	i = 0 # counter for ls1
	j = 0 # counter for ls2
	while(i < len(ls1) and j < len(ls2)):
		# do stuff until one of them runs out
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

	return ordered_list + leftover


def merge_sort(ls):
	if len(ls) == 1:
		return ls

	mid = len(ls)/2
	array_one = ls[:mid]
	array_two = ls[mid:]

	array_one = merge_sort(array_one)
	array_two = merge_sort(array_two)

	return merge(array_one, array_two)


if __name__ == '__main__':
    import numpy as np
    x = np.arange(21)
    np.random.shuffle(x)
    print x.tolist()
    quick_sort(x.tolist())
