def narcissistic( value ):
    # Code away
    value = str(value)
    
    topower = len(value)
    
    num = 0
    
    for x in value:
        num += int(x)**topower
    
    return int(value) == num
