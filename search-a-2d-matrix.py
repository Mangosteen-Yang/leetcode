def searchMatrix(martix, target):
	if len(martix) == 0:
		return False
	column = []
	for each in martix:
		column.append(each[0])

	if len(column) == 0:
		return False
	start = 0
	end = len(column)-1
	middle = 0
	while (start + 1 < end):
		middle = (start + end)/2
		if column[middle] >= target:
			end = middle
		elif column[middle] < target:
			start = middle
	if column[start] > target:
		return False
	elif target >= column[end]:
		line = end
	else:
		line = start



	if len(martix[line]) == 0:
		return False
	start = 0
	end = len(martix[line])-1
	middle = 0
	while (start + 1 < end):
		middle = (start + end)/2
		if martix[line][middle] >= target:
			end = middle
		elif martix[line][middle] < target:
			start = middle
	if martix[line][start] == target:
		return True
	elif martix[line][end] == target:
		return True
	else:
		return False
	



print searchMatrix([

    [1, 3, 5, 7],

    [10, 11, 16, 20],

    [23, 30, 34, 50]

], 3)