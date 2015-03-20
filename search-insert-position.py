#Accepted search-insert-position   340 ms	Python
def searchInsert(A, target):
	if len(A) == 0:
		return 0
	start = 0
	end = len(A)-1
	middle = 0
	if A[0] > target:
		return 0
	if A[end] < target:
		return end+1
	while (start + 1 < end):
		middle = (start + end)/2
		if A[middle] >= target:
			end = middle
		elif A[middle] < target:
			start = middle
	if A[start] == target:
		return start
	elif A[end] == target:
		return end
	else:
		return start+1

print searchInsert([], 9)
