def longest_consec(strarr, k):
    # your code
    possiblelist = []

    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""

    for i in range(len(strarr)):
        if i+k == len(strarr)+1:
            break
        possiblelist.append("".join(strarr[i:i+k]))

    maxlength = max(possiblelist,key=len)
    return maxlength
