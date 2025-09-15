def smallest_diff(x, y, z):
    diff1 = abs(x - y)

    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)

    print('smallest_diff inputs:', x, y, z)

    return min_diff


smallest_diff(3, 9, 5)


