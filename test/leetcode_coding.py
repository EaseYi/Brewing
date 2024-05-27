from collections import deque
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = deque()
        j = 0
        for x in pushed:
            stk.append(x)
            while stk and stk[-1] == popped[j]:
                stk.pop()
                j += 1
        return j == len(popped)
