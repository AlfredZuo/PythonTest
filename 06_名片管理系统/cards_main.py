import cards_tools

loop = 0
while loop < 1:
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1、新建名片")
    print("2、显示全部")
    print("3、查询名片")
    print("")
    print("0、退出系统")
    print("*" * 50)
    choice = input("请输入您的选择")
    if choice == "0":
        print("您输入的是%s, 现在退出系统" % choice)
        break
    elif choice == "1":
        print("您输入的是%s, 现在启动“新建名片操作”" % choice)
        cards_tools.cards_function_new_card()
    elif choice == "2":
        print("您输入的是%s, 现在启动“显示名片操作”" % choice)
        cards_tools.cards_function_list_all_cards()
    elif choice == "3":
        print("您输入的是%s, 现在启动“查询名片操作”" % choice)
        cards_tools.cards_function_query_card()
    else:
        print("您输入的是%s,无法处理您的请求，请重新输入" % choice)
        continue
