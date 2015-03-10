class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return len(self.items)==0
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop() 
  def peek(self):
    if not self.isEmpty():
      return self.items[len(self.items)-1]
  def size(self):
    return len(self.items)
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = Stack()
        for each in s:
            if each=='(' or each =='{' or each=='[':
                stack.push(each)
            elif not stack.isEmpty():
                if stack.peek()=='(' and each==')':
                    stack.pop()
                elif stack.peek()=='{' and each=='}':
                    stack.pop()
                elif stack.peek()=='[' and each==']':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return stack.isEmpty()