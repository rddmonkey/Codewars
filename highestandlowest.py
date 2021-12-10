def high_and_low(numbers):
    testlist = [int(x) for x in numbers.split()]
    testlist.sort()

    return f"{testlist[-1]} {testlist[0]}"
