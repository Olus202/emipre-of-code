def rotate_list(elements, rotates):
    new_elements = elements[rotates:] + elements[:rotates]
    
    return new_elements