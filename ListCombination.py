def list_combination(list1, list2):
    result = []
    for i in list1:
        index_num = list1.index(i)
        result.append(i)
        result.append(list2[index_num])
    return result
