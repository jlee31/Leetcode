class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {']', ')', '}'}
        stk = []
        for ch in s:
            if ch in hmap:
                if len(stk) == 0:
                    return False
                if stk[-1] == '(' and ch != ')':
                    return False
                if stk[-1] == '[' and ch != ']':
                    return False
                if stk[-1] == '{' and ch != '}':
                    return False
                stk.pop()
            else:
                stk.append(ch)
        if len(stk) == 0:
            return True
        else:
            return False
