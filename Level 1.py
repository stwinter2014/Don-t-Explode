import pygame
import random
import Sprites

def Level_1():
    pygame.init()
    size = [900,630]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Don't explode")
    done = False
    clock = pygame.time.Clock()
    black = (0,0,0)
    white = (255, 255, 255)
    x_g_check = False
    y_g_check = False
    x_g_speed = 0
    y_g_speed = 0

    x_g1_check = False
    y_g1_check = False
    x_g1_speed = 0
    y_g1_speed = 0
    
    x_b_check = False
    y_b_check = False
    x_b_speed = 0
    y_b_speed = 0

    x_b1_check = False
    y_b1_check = False
    x_b1_speed = 0
    y_b1_speed = 0
    
    x_r_check = False
    y_r_check = False
    x_r_speed = 0
    y_r_speed = 0

    x_r1_check = False
    y_r1_check = False
    x_r1_speed = 0
    y_r1_speed = 0
    
    x_y_check = False
    y_y_check = False
    x_y_speed = 0
    y_y_speed = 0

    x_y1_check = False
    y_y1_check = False
    x_y1_speed = 0
    y_y1_speed = 0
    
    stop = False
    final_rect_x = 0
    final_rect_y = 0
    timer = 0
    pressed = False
    exp1_pos = 0
    exp2_pos = 0
    image_evol = 0
    score = 0
    claw_image = pygame.image.load("Claw.png").convert()
    claw_list = pygame.sprite.Group()
    claw = Sprites.Claw()
    
    font = pygame.font.Font(None, 35)
    
    claw.rect.x = size[0]//2 - claw_image.get_width()//2
    claw.rect.y = size[1]//2 - claw_image.get_height()//2
    claw_list.add(claw)
    
    explosion_list = pygame.sprite.Group()
    explosion = Sprites.Explosion(exp1_pos, exp2_pos)
    explosion_list.add(explosion)
    
    seed_image = pygame.image.load("seed.png").convert()
    
    seed_list = pygame.sprite.Group()
    seed = Sprites.Seed()
    seed.rect.x = random.randint(0, size[0] - claw_image.get_width())
    seed.rect.y = random.randint(0, size[1] - claw_image.get_height())
    seed_list.add(seed)
    
    guy_green = pygame.image.load("pong1_1.png").convert()
    pong_all_list = pygame.sprite.Group()
    pong_green_list = pygame.sprite.Group()
    pong_green = Sprites.Pong_green()
    pong_green.rect.x = random.randint(0, 7)
    pong_green.rect.y = random.randint(0, size[1] - guy_green.get_height())
    pong_green_list.add(pong_green)
    pong_all_list.add(pong_green)

    pong_green1_list = pygame.sprite.Group()
    pong_green1 = Sprites.Pong_green()
    pong_green1.rect.x = random.randint(size[0] - guy_green.get_width() - 7, size[0] - guy_green.get_width())
    pong_green1.rect.y = random.randint(0, size[1] - guy_green.get_height())
    pong_green1_list.add(pong_green1)
    pong_all_list.add(pong_green1)
    
    pong_blue_list = pygame.sprite.Group()
    pong_blue = Sprites.Pong_blue()
    pong_blue.rect.x = random.randint(0, size[0] - guy_green.get_width())
    pong_blue.rect.y = random.randint(0, 7)
    pong_blue_list.add(pong_blue)
    pong_all_list.add(pong_blue)

    pong_blue1_list = pygame.sprite.Group()
    pong_blue1 = Sprites.Pong_blue()
    pong_blue1.rect.x = random.randint(0, size[0] - guy_green.get_width())
    pong_blue1.rect.y = random.randint(size[1] - guy_green.get_height() - 7, size[1] - guy_green.get_height())
    pong_blue1_list.add(pong_blue1)
    pong_all_list.add(pong_blue1)
    
    pong_red_list = pygame.sprite.Group()
    pong_red = Sprites.Pong_red()
    pong_red.rect.x = random.randint(0, 7)
    pong_red.rect.y = random.randint(0, size[1] - guy_green.get_height())
    pong_red_list.add(pong_red)
    pong_all_list.add(pong_red)

    pong_red1_list = pygame.sprite.Group()
    pong_red1 = Sprites.Pong_red()
    pong_red1.rect.x = random.randint(size[0] - guy_green.get_width() - 7, size[0] - guy_green.get_width())
    pong_red1.rect.y = random.randint(0, size[1] - guy_green.get_height())
    pong_red1_list.add(pong_red1)
    pong_all_list.add(pong_red1)
    
    pong_yellow_list = pygame.sprite.Group()
    pong_yellow = Sprites.Pong_yellow()
    pong_yellow.rect.x = random.randint(0, size[0] - guy_green.get_width())
    pong_yellow.rect.y = random.randint(0, 7)
    pong_yellow_list.add(pong_yellow)
    pong_all_list.add(pong_yellow)

    pong_yellow1_list = pygame.sprite.Group()
    pong_yellow1 = Sprites.Pong_yellow()
    pong_yellow1.rect.x = random.randint(0, size[0] - guy_green.get_width())
    pong_yellow1.rect.y = random.randint(size[1] - guy_green.get_height() - 7, size[1] - guy_green.get_height())
    pong_yellow1_list.add(pong_yellow1)
    pong_all_list.add(pong_yellow1)
    
    explode_sound = pygame.mixer.Sound("pop.wav")
    plus_sound = pygame.mixer.Sound("plus.wav")
    background = pygame.image.load('background.jpg').convert()
    gameover = pygame.image.load('gameover.jpg').convert()
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.blit(background, [0,0])
        timer += 1
        if pong_green.rect.x >= size[0] - guy_green.get_width():
            x_g_check = True
        elif pong_green.rect.x <= 0:
            x_g_check = False
        if pong_green.rect.y >= size[1] - guy_green.get_height():
            y_g_check = True
        elif pong_green.rect.y <= 0:
            y_g_check = False
        if x_g_check == True:
            x_g_speed = - random.randint(0,3)
        elif x_g_check == False:
            x_g_speed = random.randint(0, 3)
        if y_g_check == True:
            y_g_speed = - random.randint(0,3)
        elif y_g_check == False:
            y_g_speed = random.randint(0,3)

        if pong_green1.rect.x >= size[0] - guy_green.get_width():
            x_g1_check = True
        elif pong_green1.rect.x <= 0:
            x_g1_check = False
        if pong_green1.rect.y >= size[1] - guy_green.get_height():
            y_g1_check = True
        elif pong_green1.rect.y <= 0:
            y_g1_check = False
        if x_g1_check == True:
            x_g1_speed = - random.randint(0,3)
        elif x_g1_check == False:
            x_g1_speed = random.randint(0, 3)
        if y_g1_check == True:
            y_g1_speed = - random.randint(0,3)
        elif y_g1_check == False:
            y_g1_speed = random.randint(0,3)

        if pong_blue.rect.x >= size[0] - guy_green.get_width():
            x_b_check = True
        elif pong_blue.rect.x <= 0:
            x_b_check = False
        if pong_blue.rect.y >= size[1] - guy_green.get_height():
            y_b_check = True
        elif pong_blue.rect.y <= 0:
            y_b_check = False
        if x_b_check == True:
            x_b_speed = - random.randint(0,3)
        elif x_b_check == False:
            x_b_speed = random.randint(0, 3)
        if y_b_check == True:
            y_b_speed = - random.randint(0,3)
        elif y_b_check == False:
            y_b_speed = random.randint(0,3)

        if pong_blue1.rect.x >= size[0] - guy_green.get_width():
            x_b1_check = True
        elif pong_blue1.rect.x <= 0:
            x_b1_check = False
        if pong_blue1.rect.y >= size[1] - guy_green.get_height():
            y_b1_check = True
        elif pong_blue1.rect.y <= 0:
            y_b1_check = False
        if x_b1_check == True:
            x_b1_speed = - random.randint(0,3)
        elif x_b1_check == False:
            x_b1_speed = random.randint(0, 3)
        if y_b1_check == True:
            y_b1_speed = - random.randint(0,3)
        elif y_b1_check == False:
            y_b1_speed = random.randint(0,3)

        if pong_red.rect.x >= size[0] - guy_green.get_width():
            x_r_check = True
        elif pong_red.rect.x <= 0:
            x_r_check = False
        if pong_red.rect.y >= size[1] - guy_green.get_height():
            y_r_check = True
        elif pong_red.rect.y <= 0:
            y_r_check = False
        if x_r_check == True:
            x_r_speed = - random.randint(0,3)
        elif x_r_check == False:
            x_r_speed = random.randint(0, 3)
        if y_r_check == True:
            y_r_speed = - random.randint(0,3)
        elif y_r_check == False:
            y_r_speed = random.randint(0,3)

        if pong_red1.rect.x >= size[0] - guy_green.get_width():
            x_r1_check = True
        elif pong_red1.rect.x <= 0:
            x_r1_check = False
        if pong_red1.rect.y >= size[1] - guy_green.get_height():
            y_r1_check = True
        elif pong_red1.rect.y <= 0:
            y_r1_check = False
        if x_r1_check == True:
            x_r1_speed = - random.randint(0,3)
        elif x_r1_check == False:
            x_r1_speed = random.randint(0, 3)
        if y_r1_check == True:
            y_r1_speed = - random.randint(0,3)
        elif y_r1_check == False:
            y_r1_speed = random.randint(0,3)

        if pong_yellow.rect.x >= size[0] - guy_green.get_width():
            x_y_check = True
        elif pong_yellow.rect.x <= 0:
            x_y_check = False
        if pong_yellow.rect.y >= size[1] - guy_green.get_height():
            y_y_check = True
        elif pong_yellow.rect.y <= 0:
            y_y_check = False
        if x_y_check == True:
            x_y_speed = - random.randint(0,3)
        elif x_y_check == False:
            x_y_speed = random.randint(0, 3)
        if y_y_check == True:
            y_y_speed = - random.randint(0,3)
        elif y_y_check == False:
            y_y_speed = random.randint(0,3)

        if pong_yellow1.rect.x >= size[0] - guy_green.get_width():
            x_y1_check = True
        elif pong_yellow1.rect.x <= 0:
            x_y1_check = False
        if pong_yellow1.rect.y >= size[1] - guy_green.get_height():
            y_y1_check = True
        elif pong_yellow1.rect.y <= 0:
            y_y1_check = False
        if x_y1_check == True:
            x_y1_speed = - random.randint(0,3)
        elif x_y1_check == False:
            x_y1_speed = random.randint(0, 3)
        if y_y1_check == True:
            y_y1_speed = - random.randint(0,3)
        elif y_y1_check == False:
            y_y1_speed = random.randint(0,3)
        seed_hit_list = pygame.sprite.spritecollide(claw, seed_list, True)
        for seed in seed_hit_list:
            score += 1
            plus_sound.play()
            seed = Sprites.Seed()
            seed.rect.x = random.randint(0, size[0] - claw_image.get_width())
            seed.rect.y = random.randint(0, size[1] - claw_image.get_height())
            seed_list.add(seed)
        if timer > 180:
            claw_hit_list = pygame.sprite.spritecollide(claw, pong_all_list, False)
            for pong_green in claw_hit_list:
                explode_sound.play()
                stop = True
                final_rect_x = pygame.mouse.get_pos()[0]
                final_rect_y = pygame.mouse.get_pos()[1]
                pressed = True
                exp1_pos = final_rect_x
                exp2_pos = final_rect_y
                claw_list.remove(claw)
            for pong_blue in claw_hit_list:
                explode_sound.play()
                stop = True
                pressed = True
                exp1_pos = final_rect_x
                exp2_pos = final_rect_y
                claw_list.remove(claw)
            for pong_red in claw_hit_list:
                explode_sound.play()
                stop = True
                pressed = True
                exp1_pos = final_rect_x
                exp2_pos = final_rect_y
                claw_list.remove(claw)
            for pong_yellow in claw_hit_list:
                explode_sound.play()
                stop = True
                pressed = True
                exp1_pos = final_rect_x
                exp2_pos = final_rect_y
                claw_list.remove(claw)
        if stop == False:
            pong_green_list.update(x_g_speed, y_g_speed)
            pong_green1_list.update(x_g1_speed, y_g1_speed)
            pong_blue_list.update(x_b_speed, y_b_speed)
            pong_blue1_list.update(x_b1_speed, y_b1_speed)
            pong_red_list.update(x_r_speed, y_r_speed)
            pong_red1_list.update(x_r1_speed, y_r1_speed)
            pong_yellow_list.update(x_y_speed, y_y_speed)
            pong_yellow1_list.update(x_y1_speed, y_y1_speed)
            claw.rect.x = pygame.mouse.get_pos()[0] - claw_image.get_width()//2
            claw.rect.y = pygame.mouse.get_pos()[1] - claw_image.get_height()//2
        elif stop == True:
            screen.blit(gameover, [size[0]//2 - gameover.get_width()//2, size[1]//2 - gameover.get_height()//2])
            claw.rect.x = final_rect_x
            claw.rect.y = final_rect_y
        if pressed == True:
            image_evol += 1
            explosion_list.update(exp1_pos, exp2_pos, image_evol)
            explosion_list.draw(screen)
            if image_evol >= 26:
                pressed = False
                image_evol = 0
        text = font.render ("Score: ", True, white)
        text1 = font.render(str(score), True, white)
        screen.blit(text,[550, 30])
        screen.blit(text1, [650,30])
        pong_green_list.draw(screen)
        pong_green1_list.draw(screen)
        pong_blue_list.draw(screen)
        pong_blue1_list.draw(screen)
        pong_red_list.draw(screen)
        pong_red1_list.draw(screen)
        pong_yellow_list.draw(screen)
        pong_yellow1_list.draw(screen)
        claw_list.draw(screen)
        seed_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
Level_1()
