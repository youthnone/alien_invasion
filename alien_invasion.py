import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen =pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    # 创建一群外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    # 创建Play按钮
    play_button = Button(ai_settings,screen,"Play")



    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets, stats, play_button, aliens,sb)
        if stats.game_active:
            # 更新飞船
            ship.update()
            if ai_settings.is_const_shoot:
                gf.fire_bullet(ai_settings,screen,ship,bullets)
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets,stats,sb)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
        #绘制屏幕
        gf.update_screen(ai_settings,screen,ship,bullets,aliens, stats, play_button,sb)

run_game()
