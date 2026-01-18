class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten = []
        oranges = set()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    rotten.append([row, column])
                elif grid[row][column] == 1:
                    oranges.add((row, column))
        counter = 0
        if not oranges:
            return 0
        while rotten and oranges:
            temp = []
            for i in rotten:
                if (i[0] + 1, i[1]) in oranges:
                    oranges.remove((i[0] + 1, i[1]))
                    temp.append([i[0] + 1, i[1]])
                if (i[0], i[1] - 1) in oranges:
                    oranges.remove((i[0], i[1] - 1))
                    temp.append([i[0], i[1] - 1])
                if (i[0] - 1, i[1]) in oranges:
                    oranges.remove((i[0] - 1, i[1]))
                    temp.append([i[0] - 1, i[1]])
                if (i[0], i[1] + 1) in oranges:
                    oranges.remove((i[0], i[1] + 1))
                    temp.append([i[0], i[1] + 1])
            if temp:
                counter += 1
            rotten = temp
            temp = []
        if oranges:
            return -1
        return counter