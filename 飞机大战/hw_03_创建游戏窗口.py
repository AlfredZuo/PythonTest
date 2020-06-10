import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1、加载图像数据,这里并不使用文件命令操作
# file = open("./images/background.png")
# text = file.read()
# # print(text)
# file.close()
bg = pygame.image.load("./images/background.png")
# 2、blit绘制图像数据,在屏幕左上角绘制
screen.blit(bg, (0, 0))
# 3、update更新屏幕显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (190, 550))
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()
