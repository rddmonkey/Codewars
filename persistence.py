def persistence(n):
    # your code

    nums = []
    result = 1

    if n < 10:
        return n

    while n > 10:
        nums.append(n% 10)
        n = n // 10

    if len(nums) != 0:
        nums.append(n)

    for x in nums:
        result *= x

    if result < 10:
        return n

    if result > 10:
        n = result
        persistence(n)
