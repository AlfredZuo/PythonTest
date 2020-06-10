import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1、加载图像数据,这里并不使用文件命令操作
bg = pygame.image.load("./images/background.png")
# 2、blit绘制图像数据,在屏幕左上角绘制
screen.blit(bg, (0, 0))
# 3、update更新屏幕显示，最终统一显示，这里不再调用，能够提升游戏的屏幕绘制效率
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (190, 550))
pygame.display.update()

# 创建始终对象
clock = pygame.time.Clock()
i = 0

# 游戏循环 ->意味着游戏的正式开始
while True:
    # 设置刷新频率，可以指定循环体内部的代码执行的频率
    clock.tick(60)
    print(i)
    i += 1
    pass

pygame.quit()
