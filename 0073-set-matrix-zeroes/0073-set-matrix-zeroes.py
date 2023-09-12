class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        n = len(matrix[0])
        iarr = set()
        jarr = set()

        for i in range(N):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in iarr:
                        iarr.add(i)
                    if j not in jarr:
                        jarr.add(j)

        for val in iarr:
            for j in range(n):
                matrix[val][j] = 0
        for val in jarr:
            for i in range(N):
                matrix[i][val] = 0
        return matrix