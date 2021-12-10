def high_and_low(numbers):

    word = ""
    low = float("inf")
    high = float("-inf")

    for x in numbers:
        if x != " ":
            word += x
        if x == " ":
            word = int(word)
            if word > high:
                high = word
            if word < low:
                low = word
            word = ""
    if word != "":
        if int(word) > high:
            high = word
        if int(word) < low:
            low = word

    return f"{str(high)} {str(low)}"
