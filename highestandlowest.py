def high_and_low(numbers):
    listnum = []

    word = ""

    for x in numbers:
        if x != " ":
            word += x
        if x == " ":
            listnum.append(int(word))
            word = ""
    if word != "":
        listnum.append(int(word))

    low = min(listnum)
    high = max(listnum)

    return f"{str(high)} {str(low)}"
