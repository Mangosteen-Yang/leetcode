class Solution:
    # @return a boolean
    def isValid(self, s):
        stack=[]
        para={
        '(':')',
        '{':'}',
        '[':']'
        }
        for each in s:
            if each in para:
                stack.append(each)
            elif len(stack)>0 and each==para[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
                

test = Solution()
print test.isValid("[{}()()(){]")