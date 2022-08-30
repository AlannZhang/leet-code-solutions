# Given an integer numRows, return the first numRows of Pascal's triangle.

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def pascalsTriangle(numRows):
    finalList = [[1], [1, 1]]

    if numRows == 1:
        return [[1]]

    if numRows == 2:
        return finalList

    for i in range(2, numRows):
        prevRow = finalList[i - 1]
        subList = [1]

        for j in range(1, len(prevRow)):
            subList.append(prevRow[j - 1] + prevRow[j])

        subList.append(1)           
        finalList.append(subList)

    return finalList
