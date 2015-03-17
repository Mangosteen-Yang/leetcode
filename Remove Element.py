def removeElement(A, elem):
    # write your code here
    result = []
    for each in A:
        if each != elem:
            result.append(each)
    return len(result)

print removeElement([4,5], 4)