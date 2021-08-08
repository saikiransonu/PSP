def getSpiralMatrix(InputMatrix):
    result = []
    if len(InputMatrix)==0:
        return result

    row_begin =0
    row_end = len(InputMatrix)-1
    col_begin = 0
    col_end = len(InputMatrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range (col_begin,col_end+1):
            result.append(InputMatrix[row_begin][i])
        row_begin +=1
        for i in range (row_begin,row_end+1):
            result.append(InputMatrix)