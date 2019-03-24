import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen =pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        #更新飞船和子弹的位置
        ship.undate()
        bullets.update()

        #删除已消失的子弹
        for bullet in bullets.copy():
            if  bullet.rect.bottom <= 0:
            #从副本里拿到超出屏幕子弹的索引，根据索引找到原列表，并移除！！
                bullets.remove(bullet)
        #绘制屏幕
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
