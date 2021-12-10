def move_zeros(array):
    
    count = 0
    
    for x in array:
        if x == 0:
            count += 1
    
    array.extend([0]*count)
    
    while count != 0:
        array.remove(0)
        count -= 1
     
    return array
