def create_phone_number(n):
    # your code here
    n.insert(0, "(")
    n.insert(4, ")")
    n.insert(5, " ")
    n.insert(9,"-")
    ans = ""

    for x in n:
        ans += str(x)

    return ans
