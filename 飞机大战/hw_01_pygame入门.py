import pygame

pygame.init()

# 编写游戏的代码
print("pygame 已经启动")
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点是 %d, %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸是 %d, %d" % (hero_rect.width, hero_rect.height))
# size 属性返回的是一个元组
print("英雄的尺寸是 %d, %d" % hero_rect.size)


# 退出并写在pygame的模块
pygame.quit()
