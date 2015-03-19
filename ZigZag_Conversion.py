#coding:utf-8
'''
注意事项：考虑nRows=1等临界情况
考虑i 和 x各自循环次数，可以富余不可以不够
简单合并排序是不可靠的，因为(1, 11)和(11, 1)合并后均为111
'''
def convert(self, s, nRows):
	positionx = []
	positiony = []
	result = ''
	if nRows == 1:
		return s
	lineNum = (len(s)/(2*nRows-2))+1
	for i in xrange(0,lineNum*(nRows-1), nRows-1):
		for x in xrange(0,2*nRows-2):
			if(x<nRows):
				positionx.append('%d' % (x))
				positiony.append('%d' % (i))
			else:
				i+=1
				x=2*nRows-2-x
				positionx.append('%d' % (x))
				positiony.append('%d' % (i))
	sToList = list(s)
	for each in xrange(0,len(positionx)):
		positionx[each] = int(positionx[each])
	for each in xrange(0,len(positiony)):
		positiony[each] = int(positiony[each])
	tmp = zip(positionx, positiony, s)
	# tmp.sort(key=itemgetter(0,1))
	tmp = sorted(tmp, key=lambda student : student[0])
	for each in tmp:
		result+=each[2]
	return result


print convert(0, 'Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.', 3)