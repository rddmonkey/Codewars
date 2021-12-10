def duplicate_encode(word):
    word = word.upper()
    mydict = {}
    ans = ""

    for x in word:
        if x not in mydict:
            mydict[x] = 1
        else:
            mydict[x] += 1

    for x in word:
        if mydict[x] == 1:
            ans += "("
        else:
            ans += ")"

    return ans
