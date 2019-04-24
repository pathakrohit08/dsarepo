from main import *

class Solution:
    def nextLargerNodes(self,nums):
        cache, st = {}, []
        for idx,x in enumerate(nums):
            while st and st[-1][1] < x:
                a,b = st.pop()
                cache[a] = x
            st.append((idx,x))
        for idx,x in enumerate(nums):
            while st and st[-1][1] < x:
                a,b = st.pop()
                cache[a] = x
            st.append((idx,x))
        result = [-1]*len(nums)
        for idx,x in enumerate(nums):
            if idx in cache:
                result[idx] = cache[idx]
        print(result)
s=Solution()
s.nextLargerNodes([2,7,4,3,5])
s.nextLargerNodes([2,1,5])
s.nextLargerNodes([[1,7,5,1,9,2,5,1]])
                

                