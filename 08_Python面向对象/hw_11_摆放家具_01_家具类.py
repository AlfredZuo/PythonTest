class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "【%s】的面积大小是【%.1f】" % (self.name, self.area)
