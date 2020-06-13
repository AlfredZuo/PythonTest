row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d =%2d" % (row, col, row*col), end=";\t")     # 这个语法可关注一下
        col += 1
    print("")
    row += 1
