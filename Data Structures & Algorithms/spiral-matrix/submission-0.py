class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        if not matrix: 
            return ret
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        r = 0
        c = 0
        direction = 0 
        #right = 0 left = 1 top = 2 bot = 3


        while left <= right and top <= bottom:
            # right
            if direction == 0 and c < right:
                ret.append(matrix[r][c])
                c += 1
            elif direction == 0 and c == right:
                ret.append(matrix[r][c])
                direction = 3
                r += 1
                top += 1

            # down
            elif direction == 3 and r < bottom:
                ret.append(matrix[r][c])
                r += 1
            elif direction == 3 and r == bottom:
                ret.append(matrix[r][c])
                c -= 1            # step left, not down
                direction = 1
                right -= 1

            # left
            elif direction == 1 and c > left:
                ret.append(matrix[r][c])
                c -= 1
            elif direction == 1 and c == left:
                ret.append(matrix[r][c])
                r -= 1
                direction = 2
                bottom -= 1

            # up
            elif direction == 2 and r > top:
                ret.append(matrix[r][c])
                r -= 1
            elif direction == 2 and r == top:
                ret.append(matrix[r][c])
                c += 1
                direction = 0
                left += 1
            
            #
            else:
                break
        
        return ret


