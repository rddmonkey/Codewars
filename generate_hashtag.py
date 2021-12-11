def generate_hashtag(s):
    # your code here

    if s == "" or len(s) > 140:
        return False

    ans = ""
    result = ""

    for i in range(len(s)):
        if s[i].isalpha():

            if ans == "":
                letter = s[i]
                ans += letter.capitalize()
            else:
                ans += s[i].lower()
        if not s[i].isalpha():
            result += ans
            ans = ""
        if i == len(s) - 1 and ans:
            result += ans

    if result == True:
        if result[0] == "#":
            return result
    else:
        return f"#{result}"
