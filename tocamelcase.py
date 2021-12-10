def to_camel_case(text):
    # your code here

    testlist = []
    
    word = ""
    
    for i in range(len(text)):
        if i == 0:
            word += text[i]
            continue
        if text[i] == "_" or text[i] == "-":
            testlist.append(word.title())
            word = ""
        else:
            word += test[i]
    
    return "".join(testlist)
