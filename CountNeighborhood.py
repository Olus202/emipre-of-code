def count_neighborhood(tup, row, column):
    points = 0
    list_i = [(row - 1, column - 1), (row - 1, column), (row - 1, column + 1),
              (row, column - 1), (row, column), (row, column + 1),
              (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)]
    for i in list_i:
        index_i = list_i.index(i)
        r = list_i[index_i][0]
        c = list_i[index_i][1]
        if (r >= 0 or c >= 0) and (r < len(tup) or c < len(tup[0])):
            if tup[r][c] or tup[r][c] == 1:
                points += 1
            if tup[row][column] == 1:
                points -= 1
            else:
                pass
        else:
            pass
    return points
