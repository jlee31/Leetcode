class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ret = 0
        for i in range(len(tokens)):
            if (tokens[i] == '+'):
                val1 = stk.pop()
                val2 = stk.pop()
                tmp = val1 + val2
                stk.append(tmp)
            elif (tokens[i] == '*'):
                val1 = stk.pop()
                val2 = stk.pop()
                tmp = val1 * val2
                stk.append(tmp)
            elif (tokens[i] == '-'):
                val1 = stk.pop()
                val2 = stk.pop()
                tmp = val2 - val1
                stk.append(tmp)
            elif (tokens[i] == '/'):
                val1 = stk.pop()
                val2 = stk.pop()
                tmp = int(val2 / val1)
                stk.append(tmp)
            else:
                stk.append(int(tokens[i]))
        return stk[-1]