#Accepted	search-for-a-range	457 ms	Python
def searchRange(A, target):
	if len(A) == 0:
		return [-1, -1]
	start = 0
	end = len(A)-1
	middle = 0
	while (start + 1 < end):
		middle = (start + end)/2
		if A[middle] >= target:
			end = middle
		elif A[middle] < target:
			start = middle
	if A[start] == target:
		r_start = start
	elif A[end] == target:
		r_start = end
	else:
		r_start = -1

	start = 0
	end = len(A)-1
	middle = 0
	while (start + 1 < end):
		middle = (start + end)/2
		if A[middle] > target:
			end = middle
		elif A[middle] <= target:
			start = middle
	if A[end] == target:
		r_end = end
	elif A[start] == target:
		r_end = start
	else:
		r_end = -1

	return r_start, r_end

print searchRange([], 8)




