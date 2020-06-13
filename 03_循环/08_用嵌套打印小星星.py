# 在控制台连续输出五行 *，每一行星号的数量依次递增
# *
# **
# ***
# ****
# *****
row = 1

while row <= 5:
    col = 1
    while col <= row:
        print("* ", end="")     # 这个语法可关注一下
        col += 1
    print("")
    row += 1
