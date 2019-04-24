'''921. Minimum Add to Make Parentheses Valid'''
from main import *
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack)==0
        
class Solution:
    def minAddToMakeValid(self,S):
        if S:
            c=0
            s=Stack()
            for _ in S:
                if _ in '(':
                    s.push(_)
                else:
                    if not s.isEmpty():
                        s.pop()
                    else:
                        c+=1

            return c+s.size()

s=Solution()
brackets=['())','(((','()','()))((']
for b in brackets:
    print('{} is {}'.format(b,s.minAddToMakeValid(b)))