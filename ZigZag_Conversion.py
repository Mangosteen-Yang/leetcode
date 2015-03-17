def convert(self, s, nRows):
	position = []
	result = ''
	if nRows == 1:
		return s
	lineNum = (len(s)/(2*nRows-2))+2
	print lineNum
	for i in xrange(0,2*lineNum-1, nRows-1):
		for x in xrange(0,2*nRows-2):
			if(x<nRows):
				position.append('%d%d'%(x, i))
			else:
				i+=1
				x=2*nRows-2-x
				position.append('%d%d'%(x, i))
	sToList = list(s)
	tmp = zip(position, s)
	tmp.sort()
	for each in tmp:
		result+=each[1]
	return result


print convert(0, 'PAYPALISHIRING', 6)