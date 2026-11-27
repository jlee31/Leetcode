class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        p_len = len(p)
        s_len = len(s)

        def memo(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # Pattern exhausted
            if j == p_len:
                return i == s_len

            # Check whether current characters match
            first_match = (
                i < s_len and
                (s[i] == p[j] or p[j] == ".")
            )

            # Handle *
            if j + 1 < p_len and p[j + 1] == "*":
                zero_occurrences = memo(i, j + 2)

                one_or_more = (
                    first_match and memo(i + 1, j)
                )

                cache[(i, j)] = zero_occurrences or one_or_more
                return cache[(i, j)]

            # Normal character matching
            res = first_match and memo(i + 1, j + 1)

            cache[(i, j)] = res
            return res

        return memo(0, 0)