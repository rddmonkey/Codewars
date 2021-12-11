def generate_hashtag(s):
    # your code here

    if s == "" or len(s) > 140:
        return False

    ans = ""

    for i in range(len(s)):
        if s[i].isalpha():
            if ans == "":
                ans += s[i].capitalize
            else:
                ans += s[i]
        if not s[i].isalpha():
            ans = ""
    
    if ans[0] == "#":
        return ans
    else:
        return f"#{ans}"
