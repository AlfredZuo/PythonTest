class Game(object):
    # 历史最高分，类属性
    top_score = 0

    def __init__(self, player_name):
        # 实例属性
        self.player_name = player_name

    # 静态方法
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门，布置豌豆射手发射炮弹")

    # 类方法
    @classmethod
    def show_top_score(cls):
        print("历史最高分是 %s" % cls.top_score)

    # 实例方法
    def start_game(self):
        print("%s 开始游戏了..." % self.player_name)
        print("%s 得了98分" % self.player_name)
        Game.top_score = 98


# 1.查看游戏帮助信息
Game.show_help()

# 2. 查看游戏历史最高分
Game.show_top_score()

# 3. 创建游戏对象
zwdzjs = Game("Alfred")
zwdzjs.start_game()
Game.show_top_score()
