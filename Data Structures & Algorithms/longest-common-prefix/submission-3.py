class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        n_shortest = float('inf')
        short_str = ""
        for i in range(n):
            if len(strs[i]) < n_shortest:
                n_shortest = len(strs[i])
                short_str = strs[i]
        
        out = ""
        for i in range(n_shortest):
            ltr = short_str[i]
            for string in strs:
                if ltr != string[i]:
                    return out
            out += short_str[i]

        return out