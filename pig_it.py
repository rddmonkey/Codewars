def pig_it(text):
    # your code here

    testlist = text.split()
    ans = []

    for i in range(len(testlist)):
        word = ""
        if len(testlist[i]) == 1 and testlist[i].isalpha() == False:
            ans.append(testlist[i])
            continue
        for j in range(1, len(testlist[i])):
            word += testlist[i][j]

        word += testlist[i][0] + "ay"
        ans.append(word)

    return " ".join(ans)
