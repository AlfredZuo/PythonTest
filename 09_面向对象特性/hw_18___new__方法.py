class MusicPlayer(object):

    # new是一个静态方法
    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")

        # super一定要加括号
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)
