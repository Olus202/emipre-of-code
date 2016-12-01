def transpose(data):
    row_num = len(data[0])
    field_num = len(data)
    new_data = [[0 for x in range(field_num)] for y in range(row_num)]

    for item in data:
        for i in item:
            item_index = data.index(item)
            i_index = item.index(i)
            new_item_index = i_index
            new_i_index = item_index
            new_data[new_item_index][new_i_index] = i
            data[item_index][i_index] = "a"
            
    return new_data
