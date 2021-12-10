def to_camel_case(text):
    # your code here
    testlist = []
    word = ""

    for i in range(len(text)):
        if text[i] == "-" or text[i] == "_" or i == len(text):
            testlist.append(word)
            word = ""
        else:
            if len(word) == 0 and i != 0:
                word += text[i].capitalize()
            else:
                word += text[i]

    if word != "":
        testlist.append(word)

    return "".join(testlist)
