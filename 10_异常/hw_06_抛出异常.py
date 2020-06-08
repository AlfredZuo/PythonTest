def input_password():
    pwd = input("请输入密码（密码长度最低为8位）：")

    if len(pwd) >= 8:
        print("您输入的密码是：%s" % pwd)
        return pwd

    print("~~执行到这里说明密码长度不够~~")
    ex = Exception("错误原因：密码长度不够")
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)


