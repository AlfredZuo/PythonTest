import pygame


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        # 如果一个类的父类不是object, 在重写初始化方法是，一定要先super()一下父类的__init__()方法
        # 保证父类中实现的__init__代码能够被正常的执行
        # super(GameSprite, self).__init__()
        super().__init__()

        # 定义对象的属性
        # get_rect()只能得到两个参数，那就是一个图像的长宽像素
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed
