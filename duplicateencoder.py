def duplicate_encode(word):
    # your code here
    mydict = {}
    ans = ""

    for x in word:
        if x not in mydict:
            mydict[x.upper()] = 1
        else:
            mydict[x.upper()] += 1

    for x in word:
        if mydict[x.upper()] == 1:
            ans += "("
        else:
            ans += ")"

    return ans
