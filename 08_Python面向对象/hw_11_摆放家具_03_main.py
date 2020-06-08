import hw_11_摆放家具_02_房间类
import hw_11_摆放家具_01_家具类

my_house = hw_11_摆放家具_02_房间类.House("一房一厅", 89)
bed = hw_11_摆放家具_01_家具类.HouseItem("席梦思", 4)
chest = hw_11_摆放家具_01_家具类.HouseItem("衣柜", 2)
table = hw_11_摆放家具_01_家具类.HouseItem("餐桌", 1.5)
void = hw_11_摆放家具_01_家具类.HouseItem("void", 80)

print(my_house)
my_house.add_item(bed)
# print(my_house)
my_house.add_item(chest)
my_house.add_item(table)
my_house.add_item(void)
print(my_house)

