class Solution:
    # @return a boolean
    def isValid(self, s):
        stack=[]
        for each in s:
            if each=='(' or each =='{' or each=='[':
                stack.append(each)
            elif len(stack)!=0:
                if stack[-1]=='(' and each==')':
                    stack.pop()
                elif stack[-1]=='{' and each=='}':
                    stack.pop()
                elif stack[-1]=='[' and each==']':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack

test = Solution()
print test.isValid("[{}()()()(){}]")