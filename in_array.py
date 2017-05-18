def in_array(array1, array2):
    """return elements in array1 that are substrings of any elements in array2"""
    output = []
    for elementa in array1:
        for elementb in array2:
            if elementa in elementb:
                output.append(elementa)
    return sorted(list(set(output)))
