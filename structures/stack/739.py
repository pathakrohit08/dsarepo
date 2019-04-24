'''739. Daily Temperatures'''
from main import *
class Solution:
    def dailyTemperatures(self,T):
        if T:
            res=[0]*len(T)
            s=Stack()
            for i in range(len(T)):
                while not s.isEmpty() and T[s.peek()]<T[i]:
                    current_idx=s.pop()
                    result=i-current_idx
                    res[current_idx]=result
                s.push(i)

            return res

s=Solution()
s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])

        