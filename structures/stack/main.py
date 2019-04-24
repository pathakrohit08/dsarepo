'''Python code to implement stack functionality'''

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

import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack=Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

    def testSize(self):
        assert self.stack.size()==4
    
    def testPop(self):
        assert self.stack.pop()==4

    def testEmpty(self):
        assert not self.stack.isEmpty()

if __name__=='__main__':
    unittest.main()