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

# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(190, 550, 102, 126)

# 游戏循环 ->意味着游戏的正式开始
while True:
    # 设置刷新频率，可以指定循环体内部的代码执行的频率
    clock.tick(60)
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
    for event in event_list:
        if event.type == pygame.QUIT:
            print("用户点击退出游戏...")
            pygame.quit()

            # 直接终止当前正在运行的程序
            exit()

    # 2.修改飞机的位置
    hero_rect.y -= 2
    if hero_rect.y < -126:
        hero_rect.y = 700
    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 4.调用update方法更新显示
    pygame.display.update()

    pass

pygame.quit()
