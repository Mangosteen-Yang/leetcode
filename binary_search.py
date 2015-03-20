#Accepted	binary_search	440 ms	Python
def binarySearch(nums, target):
	start = 0
	end = len(nums)-1
	middle = 0
	while (start + 1 < end):
		middle = (start + end)/2
		if nums[middle] >= target:
			end = middle
		elif nums[middle] < target:
			start = middle
	if nums[start] == target:
		return start
	elif nums[end] == target:
		return end
	else:
		return -1

print binarySearch([3,4,5,8,8,8,8,10,13,14], 8)