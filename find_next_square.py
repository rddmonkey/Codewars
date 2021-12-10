def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    import math

    if math.sqrt(sq) == int(math.sqrt(sq)):
        sq = math.sqrt(sq)
        sq += 1
        sq = sq*sq
        return sq
    else:
        return -1
