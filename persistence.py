def persistence(n):
    # your code
    ans = 0

    while n >= 10:
        ans += 1
        n = str(n)
        result = 1

        for x in n:
            result *=int(x)
            n = result

    return ans
