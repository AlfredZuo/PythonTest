import hw_11_摆放家具_01_家具类


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        temp_str = ""
        for item in self.item_list:
            temp_str = temp_str + "【%s】的面积大小是【%.1f】" % (item.name, item.area) + "\r\n"
            # print("【%s】的面积大小是【%.1f】\r\n" % (item.name, item.area), file_Writer=temp_str)

        return "本房屋的房型是[%s], 房间大小[%.1f]平方米, 剩余空间[%.1f]平方米，房间内具有家具[%d]个，列表如下\r\n" \
               "%s" % (self.house_type, self.area, self.free_area, len(self.item_list), temp_str)

    def add_item(self, item):
        print("要添加 %s" % item)
        if self.free_area < item.area:
            print("房间空间不够了,不能添加")
            return
        self.free_area -= item.area
        self.item_list.append(item)
