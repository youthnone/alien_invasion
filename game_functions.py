import sys

import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 根据按键按下和松开，左右移动飞船
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)


        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)




def update_screen(ai_settings,screen,ship,bullets):
    """每次循环时都重绘屏幕"""
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # 让最近绘制的屏幕可见,即重绘屏幕
    pygame.display.flip()

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_riht = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)



def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_riht = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False