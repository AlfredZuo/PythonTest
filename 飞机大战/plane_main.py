from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序的类"""

    def __init__(self):
        print("游戏初始化...")
        pygame.init()

        # 创建游戏的窗口
        self.screen = pygame.display.set_mode((480, 700))
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 绘制背景图像
        # 1、加载图像数据,这里并不使用文件命令操作
        bg = pygame.image.load("./images/background.png")
        # 2、blit绘制图像数据,在屏幕左上角绘制
        self.screen.blit(bg, (0, 0))
        pygame.display.update()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始...")
        while True:
            self.clock.tick(60)

            pass


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
