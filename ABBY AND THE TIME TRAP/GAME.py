# Author : Ajant Surve
#

try:
    import random
    import sys
    import pygame
except Exception as e:
    print("Please run Install_Import.bat", e)
    print("Please close install and rerun...")
    key = input()


#LARGEST = (350, 300)
#SMALLEST = (150, 150)

pygame.init()

music = pygame.mixer.Sound('MUSIC.mp3')
music.play()
rect_sizes = (90, 100)

i_ro = pygame.image.load('CHARS//ROCKET_4.png')
icon = pygame.display.set_icon(i_ro)

screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

#MAIN MENU IMAGES
name = pygame.image.load('CHARS//TITLE.png')
name = pygame.transform.scale(name, (700, 200))

speed = 5

x = 400
y = 500
size_X = 225
size_y = 175

player = pygame.image.load('CHARS//ROCKET_1.png')
player = pygame.transform.scale(player, (size_X, size_y))
player_rect = player.get_rect()
player_rect.center = (x, y)
player_mask = pygame.mask.from_surface(player)

play_button = pygame.image.load('CHARS//PLAY_NT.png')
play_button = pygame.transform.scale(play_button,(450, 400))
play_rect = play_button.get_rect()
play_rect.center = (450, 700)

score_asteroid = pygame.image.load('CHARS//CRATE.png')
sizer = pygame.transform.scale(score_asteroid, (1000, 1000))

about = pygame.image.load('CHARS//ABOUT.png')
about = pygame.transform.scale(about, (1300, 700))

back_button = pygame.image.load('CHARS//BACK_NT.png')
back_button = pygame.transform.scale(back_button,(400, 400))
back_button = pygame.transform.flip(back_button, True, False)
backyrect = back_button.get_rect()
backyrect.center = (450, 200)

back_button_1 = pygame.image.load('CHARS//BACK_NT.png')
back_button_1 = pygame.transform.scale(back_button_1, (400, 400))
back_button_1 = pygame.transform.flip(back_button_1, True, False)
endrect = back_button_1.get_rect()
endrect.center = (1000, 800)

asteroid = pygame.image.load('CHARS//CRATE.png')
aster_rect = asteroid.get_rect()

quit_button = pygame.image.load('CHARS//QUIT_NT.png')
quit_button = pygame.transform.scale(quit_button,(450, 400))
quit_rect = quit_button.get_rect()
quit_rect.center = (1400, 700)

ab_button = pygame.image.load('CHARS//ABOUT_NT.png')
ab_button = pygame.transform.scale(ab_button,(450, 400))
ab_rect = ab_button.get_rect()
ab_rect.center = (930, 700)

back_image = pygame.image.load('BACKGROUND.png')

back_rect = back_image.get_rect()

point = 0
res = str(point)

font = pygame.font.Font(None, 75)
Asteroids_avoided = font.render("Asteroids Avoided:", True, (255, 255, 255))
score = font.render(res, True, (255, 255, 255))
mouse_pos = pygame.mouse.get_pos()
text = font.render(str(mouse_pos), True, (255, 0, 0))


timer_fl = 5
str_tim = str(timer_fl)
cut = str_tim[:5]
timer = font.render(cut, True, (0, 255, 0))
first_spawn = False

a_speed = 5

a_1 = pygame.image.load('CHARS//CRATE.png')
a_1 = pygame.transform.scale(a_1, (275, 275))
rect1 = a_1.get_rect()
rect1.center = (random.randrange(screen.get_width(), screen.get_width() + 50), random.randrange(75, 800))
rect1.size = rect_sizes
mask1 = pygame.mask.from_surface(a_1)

a_2 = pygame.image.load('CHARS//CRATE.png')
a_2 = pygame.transform.scale(a_2, (275, 275))
rect2 = a_2.get_rect()
rect2.center = (random.randrange(screen.get_width(), screen.get_width() + 200), random.randrange(75, 800))
rect2.size = rect_sizes
mask2 = pygame.mask.from_surface(a_2)

a_3 = pygame.image.load('CHARS//CRATE.png')
a_3 = pygame.transform.scale(a_3, (275, 275))
rect3 = a_3.get_rect()
rect3.center = (random.randrange(screen.get_width(), screen.get_width() + 20), random.randrange(75, 800))
rect3.size = rect_sizes
mask3 = pygame.mask.from_surface(a_3)

a_4 = pygame.image.load('CHARS//CRATE.png')
a_4 = pygame.transform.scale(a_4, (275, 275))
rect4 = a_4.get_rect()
rect4.center = (random.randrange(screen.get_width(), screen.get_width() + 500), random.randrange(75, 800))
rect4.size = rect_sizes
mask4 = pygame.mask.from_surface(a_4)


level = 0
while True:

    if pygame.event.get(pygame.QUIT):
        pygame.quit()
    if level == 0: #MENU
        screen.blit(back_image, back_rect)

        screen.blit(back_image, back_rect.move(back_rect.width, 0))

        screen.blit(name, (625, 150))

        screen.blit(ab_button, ab_rect)

        screen.blit(quit_button, quit_rect)

        screen.blit(play_button, play_rect)

        if play_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:

                first_spawn = True
                rect1.center = (random.randrange(screen.get_width(), screen.get_width() + 50), random.randrange(75, 800))
                rect2.center = (random.randrange(screen.get_width(), screen.get_width() + 200), random.randrange(75, 800))
                rect3.center = (random.randrange(screen.get_width(), screen.get_width() + 20), random.randrange(75, 800))
                rect4.center = (random.randrange(screen.get_width(), screen.get_width() + 500), random.randrange(75, 800))
                point = 0
                timer_fl = 5
                level = 1

            play_button = pygame.image.load('CHARS//PLAY_T.png')
            play_button = pygame.transform.scale(play_button, (450, 400))


        elif quit_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                break

            quit_button = pygame.image.load('CHARS//QUIT_T.png')
            quit_button = pygame.transform.scale(quit_button, (450, 400))

        elif ab_rect.collidepoint(pygame.mouse.get_pos()):

            if pygame.mouse.get_pressed()[0]:
                level = 2

            ab_button = pygame.image.load('CHARS//ABOUT_T.png')
            ab_button = pygame.transform.scale(ab_button, (450, 400))

        else:
            play_button = pygame.image.load('CHARS//PLAY_NT.png')
            play_button = pygame.transform.scale(play_button, (450, 400))

            quit_button = pygame.image.load('CHARS//QUIT_NT.png')
            quit_button = pygame.transform.scale(quit_button, (450, 400))

            ab_button = pygame.image.load('CHARS//ABOUT_NT.png')
            ab_button = pygame.transform.scale(ab_button, (450, 400))

    if level == 1: #PLAY
        res = str(point)
        score = font.render(res, True, (255, 255, 255))


        hit1_offset = (int(player_rect.x - rect1.x), int(player_rect.y - rect1.y))
        hit1 = mask1.overlap(player_mask, hit1_offset)

        hit2_offset = (int(player_rect.x - rect2.x), int(player_rect.y - rect2.y))
        hit2 = mask2.overlap(player_mask, hit2_offset)

        hit3_offset = (int(player_rect.x - rect3.x), int(player_rect.y - rect3.y))
        hit3 = mask3.overlap(player_mask, hit3_offset)

        hit4_offset = (int(player_rect.x - rect4.x), int(player_rect.y - rect4.y))
        hit4 = mask4.overlap(player_mask, hit4_offset)

        screen.fill((0, 0, 0))
        screen.blit(back_image, back_rect)
        screen.blit(back_image, back_rect.move(back_rect.width, 0))
        screen.blit(player, player_rect)

        screen.blit(a_1, rect1)
        rect1.x -= a_speed

        screen.blit(a_2, rect2)
        rect2.x -= a_speed

        screen.blit(a_3, rect3)
        rect3.x -= a_speed

        screen.blit(a_4, rect4)
        rect4.x -= a_speed


        timer_fl -= 0.01
        str_tim = str(timer_fl)
        cut = str_tim[:5]
        timer = font.render(cut, True, (0, 255, 0))
        screen.blit(timer, (1500, 200))
        pygame.display.update()

        if timer_fl < 0 and speed != 0.5:
            speed = speed - 0.5
            timer_fl = 5
        if speed == 0.5:
            timer = font.render("",True,(255, 255, 255))
        keys = pygame.key.get_pressed()
        if hit1:
            music.stop()
            explode = pygame.mixer.Sound('EXPLODE.mp3')
            explode.play()
            rect1.center = (random.randrange(screen.get_width(), screen.get_width() + 100), random.randrange(75, 800))
            rect1.x += 0
            level = 3
            timer_fl == 5
            print("1")
            speed = 5
        if hit2:
            music.stop()
            explode = pygame.mixer.Sound('EXPLODE.mp3')
            explode.play()
            rect2.center = (random.randrange(screen.get_width(), screen.get_width() + 100), random.randrange(75, 800))
            rect2.x += 0
            level = 3
            speed = 5
            timer_fl == 5
            print("2")
        if hit3:
            music.stop()
            explode = pygame.mixer.Sound('EXPLODE.mp3')
            explode.play()
            rect3.center = (random.randrange(screen.get_width(), screen.get_width() + 100), random.randrange(75, 800))
            rect3.x += 0
            speed = 5
            level = 3
            timer_fl == 5
            print("3")
        if hit4:
            music.stop()
            explode = pygame.mixer.Sound('EXPLODE.mp3')
            explode.play()
            rect4.center = (random.randrange(screen.get_width(), screen.get_width() + 100), random.randrange(75, 800))
            rect4.x += 0
            level = 3
            print("4")
            speed = 5
            timer_fl == 5
        if rect1.x < 0:
            point += 1
            rect1.center = (random.randrange(screen.get_width(), screen.get_width() + 100), random.randrange(75, 800))

        if rect2.x < 0:
            point += 1
            rect2.center = (random.randrange(screen.get_width(), screen.get_width() + 100), random.randrange(75, 800))

        if rect3.x < 0:
            point += 1
            rect3.center = (random.randrange(screen.get_width(), screen.get_width() + 100), random.randrange(75, 800))

        if rect4.x < 0:
            point += 1
            rect4.center = (random.randrange(screen.get_width(), screen.get_width() + 100), random.randrange(75, 800))

        if keys[pygame.K_w] and player_rect.y > 75 or keys[pygame.K_UP] and player_rect.y > 75:
            player_rect.y -= speed
        if keys[pygame.K_s] and player_rect.y < 800 or keys[pygame.K_DOWN] and player_rect.y < 800:
            player_rect.y += speed

    if level == 2:
        screen.fill((0, 0, 0))
        screen.blit(back_image, back_rect)
        screen.blit(back_image, back_rect.move(back_rect.width, 0))
        screen.blit(about, (250, 200))
        screen.blit(back_button, backyrect)
        pygame.display.update()
        if backyrect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                level = 0
            back_button = pygame.image.load('CHARS//BACK_T.png')
            back_button = pygame.transform.scale(back_button, (400, 400))
            back_button = pygame.transform.flip(back_button, True, False)
        else:
            back_button = pygame.image.load('CHARS//BACK_NT.png')
            back_button = pygame.transform.scale(back_button, (400, 400))
            back_button = pygame.transform.flip(back_button, True, False)

    if level == 3:
        screen.fill((0, 0, 0))
        screen.blit(back_image, back_rect)
        screen.blit(back_image, back_rect.move(back_rect.width, 0))
        screen.blit(sizer, (500, 50))
        screen.blit(Asteroids_avoided, (750, 300))
        screen.blit(score, (950, 400))
        screen.blit(back_button_1, endrect)
        pygame.display.update()
        if endrect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                explode.stop()
                music.play()    
                level = 0
            back_button_1 = pygame.image.load('CHARS//BACK_T.png')
            back_button_1 = pygame.transform.scale(back_button_1, (400, 400))
            back_button_1 = pygame.transform.flip(back_button_1, True, False)
        else:
            back_button_1 = pygame.image.load('CHARS//BACK_NT.png')
            back_button_1 = pygame.transform.scale(back_button_1, (400, 400))
            back_button_1 = pygame.transform.flip(back_button_1, True, False)

    if back_rect.right == 0:
        back_rect.x = 0
    clock.tick(60)
    pygame.display.flip()
    back_rect.move_ip(-2, 0)
pygame.quit()
sys.exit()