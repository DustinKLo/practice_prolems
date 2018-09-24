
def maxArea(ls):
    """
    :type height: List[int]
    :rtype: int
    """
    area = 0
    for i in range(len(ls)-1):
    	for j in range(1, len(ls[i:])):
    		left_wall = ls[i]
    		right_wall = ls[i + j]
    		
    		area_temp = j * min(left_wall, right_wall)
    		
    		if area_temp > area:
    			area = area_temp

    return area


def maxAreaFast(ls):
	left = 0
	right = len(ls) - 1
	area = 0

	while left < right:
		area_temp = (right - left) * min(ls[left], ls[right])
		area = max(area, area_temp)

		if ls[left] < ls[right]:
			left += 1
		else:
			right -= 1

	return area


if __name__ == '__main__':
	import time
	ls = [28,342,418,485,719,670,878,752,662,994,654,504,929,660,424,855,922,744,600,229,728,33,371,863,
	561,772,271,178,455,449,426,835,143,845,321,214,867,199,967,881,193,973,386,122,633,810,330,907,906,
	282,136,986,315,860,849,229,632,473,759,87,922,185,922,418,382,243,632,250,795,599,131,988,924,869,
	463,558,680,145,465,938,427,954,925,94,814,126,323,798,599,434,885,874,620,159,292,354,755,924,956,
	550,876,88,890,800,309,705,358,989,850,176,280,629,130,205,724,296,331,399,94,283,186,331,157,806,
	490,801,512,597,725,469,499,601,909,390,754,218,447,112,560,298,640,840,279,122,397,355,418,80,755,
	864,363,293,195,872,451,38,673,963,635,751,432,487,352,341,229,458,912,676,923,472,326,563,312,606]

	start = time.time()
	print(maxArea(ls))
	print(time.time() - start)

	start = time.time()
	print(maxAreaFast(ls))
	print(time.time() - start)
