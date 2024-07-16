import pygame
import time
import random

pygame.init()
modes = pygame.display.list_modes()
screen = pygame.display.set_mode()
pygame.display.toggle_fullscreen()
WIDTH, HEIGHT = screen.get_size()
clock = pygame.time.Clock()
# player2_pos =
font = pygame.font.Font('freesansbold.ttf', 40)
turn = 1
points_x = 0
points_o = 0
timea = 30
sec = 0
print('hello')
text1score = font.render('Score P1 : ' + str(points_x), True, 'green', 'purple')
text2score = font.render('Score P2 : ' + str(points_o), True, 'green', 'purple')
timetext = font.render(str(timea), True, 'green', 'purple')
p1wintext = font.render('Player 1 Wins !', True, 'green', 'purple')
p2wintext = font.render('Player 2 Wins !', True, 'green', 'purple')
textRect1 = text1score.get_rect()
textRect2 = text2score.get_rect()
textRect3 = p1wintext.get_rect()
textRect4 = p2wintext.get_rect()
power_teleport = pygame.Surface((35, 35))
power_speed = pygame.Surface((35, 35))
power_freeze = pygame.Surface((35, 35))
power_extra_time = pygame.Surface((35, 35))
power_extra_time.fill('pink')
power_speed.fill('green')
power_teleport.fill('yellow')
power_freeze.fill('cyan')
color = 'red'
skibidi = True

while skibidi:
    power_x = random.randint(1, WIDTH - 1)
    power_y = random.randint(1, HEIGHT - 1)
    power2_x = random.randint(1, WIDTH - 1)
    power2_y = random.randint(1, HEIGHT - 1)
    power3_x = random.randint(1, WIDTH - 1)
    power3_y = random.randint(1, HEIGHT - 1)
    power4_x = random.randint(1, WIDTH - 1)
    power4_y = random.randint(1, HEIGHT - 1)
    variable = True
    variable2 = False
    dt = 0
    a = True
    b = True
    po = True
    shifu = True
    tai_lung = True
    chamaeleon = True
    freeze_time_start = False
    variable2 = True
    speed1 = 7
    speed2 = 7
    player2_pos = pygame.Vector2(screen.get_width() / 2 + 300, screen.get_height() / 2)
    player_pos = pygame.Vector2(screen.get_width() / 2 - 200, screen.get_height() / 2)
    running = True
    text1score = font.render('Score P1 : ' + str(points_x), True, 'green', 'purple')
    text2score = font.render('Score P2 : ' + str(points_o), True, 'green', 'purple')
    timea = 30
    while running:
        catcher_text = font.render('The catcher is : ' + color, True, color, 'purple')
        timetext = font.render(str(timea), True, 'green', 'purple')
        erase_text = font.render('The catcher is : ' + color, True, 'purple', 'purple')
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        screen.blit(catcher_text, (300, 0))
        screen.blit(text1score, (20, 0))
        screen.blit(timetext, (790 , 0))
        screen.blit(text2score, (1200, 0))
        pygame.draw.circle(screen, "red", player_pos, 30)
        pygame.draw.circle(screen, 'blue', player2_pos, 30)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= speed1
        if keys[pygame.K_s]:
            player_pos.y += speed1
        if keys[pygame.K_a]:
            player_pos.x -= speed1
        if keys[pygame.K_d]:
            player_pos.x += speed1
        if keys[pygame.K_UP]:
            player2_pos.y -= speed2
        if keys[pygame.K_DOWN]:
            player2_pos.y += speed2
        if keys[pygame.K_LEFT]:
            player2_pos.x -= speed2
        if keys[pygame.K_RIGHT]:
            player2_pos.x += speed2
        if keys[pygame.K_r]:
            running = False
            skibidi = False

        p1upHitbox = player_pos.y - 38
        p1leftHitbox = player_pos.x - 40
        p1downHitbox = player_pos.y + 38
        p1rightHitbox = player_pos.x + 40
        p2upHitbox = player2_pos.y - 38
        p2leftHitbox = player2_pos.x - 40
        p2downHitbox = player2_pos.y + 38
        p2rightHitbox = player2_pos.x + 40
        if player_pos.x >= WIDTH:
            player_pos.x = 1
        if player_pos.x <= 0:
            player_pos.x = WIDTH - 1
        if player_pos.y >= HEIGHT:
            player_pos.y = 1
        if player_pos.y < 0:
            player_pos.y = HEIGHT - 1
        if player2_pos.x >= WIDTH:
            player2_pos.x = 1
        if player2_pos.x <= 0:
            player2_pos.x = WIDTH - 1
        if player2_pos.y >= HEIGHT:
            player2_pos.y = 1
        if player2_pos.y < 0:
            player2_pos.y = HEIGHT - 1
        if timea == 0:
            if turn % 2 == 1:
                points_o += 1
                timea = 30
                screen.blit(erase_text, (300, 0))
                screen.blit(p2wintext, (20, 0))
                pygame.display.flip()
                time.sleep(0.7)
                running = False
            else:
                points_x += 1
                timea = 30
                screen.blit(erase_text, (300, 0))
                screen.blit(p1wintext, (20, 0))
                pygame.display.flip()
                time.sleep(0.7)
                running = False
        if turn % 2 == 1:
            color = 'red'
        else :
            color = 'blue'
        if turn % 2 == 1 and variable == True:
            print('ass')
            speed1 += 1
            variable = False
        if turn % 2 == 0 and variable == True:
            print('stoobid')
            speed2 += 1
            variable = False
        if timea <= 20 and po == True:
            screen.blit(power_teleport, (power_x, power_y))
        if p1upHitbox < power_y and p1leftHitbox < power_x and p1downHitbox > power_y and p1rightHitbox > power_x and po == True:
            player_pos.x = random.randint(1, WIDTH - 1)
            player_pos.y = random.randint(1, HEIGHT - 1)
            po = False

        if p2upHitbox < power_y and p2leftHitbox < power_x and p2downHitbox > power_y and p2rightHitbox > power_x and po == True:
            player2_pos.x = random.randint(1, WIDTH - 1)
            player2_pos.y = random.randint(1, HEIGHT - 1)
            po = False
        if timea <= 25 and shifu == True:
            screen.blit(power_speed, (power2_x, power2_y))
        if p1upHitbox < power2_y and p1leftHitbox < power2_x and p1downHitbox > power2_y and p1rightHitbox > power2_x and shifu == True:
            speed1 += 4
            shifu = False
            speed_hit_time = timea
        if p2upHitbox < power2_y and p2leftHitbox < power2_x and p2downHitbox > power2_y and p2rightHitbox > power2_x and shifu == True:
            speed2 += 4
            shifu = False
            speed_hit_time = timea
        if shifu == False:
            if timea == speed_hit_time - 3:
                speed1 = 7
                speed2 = 7
        if timea <= 15 and tai_lung == True:
            screen.blit(power_freeze, (power3_x, power3_y))
        if p1upHitbox < power3_y and p1leftHitbox < power3_x and p1downHitbox > power3_y and p1rightHitbox > power3_x and tai_lung == True:
            freeze_pos_x = player2_pos.x
            freeze_pos_y = player2_pos.y
            freeze_time = timea
            tai_lung = False
            a = False
        if p2upHitbox < power3_y and p2leftHitbox < power3_x and p2downHitbox > power3_y and p2rightHitbox > power3_x and tai_lung == True:
            freeze2_pos_x = player_pos.x
            freeze2_pos_y = player_pos.y
            freeze_time = timea
            tai_lung = False
            a = True
        if timea <= 7 and chamaeleon == True:
            screen.blit(power_extra_time, (power4_x, power4_y))
        if p1upHitbox < power4_y and p1leftHitbox < power4_x and p1downHitbox > power4_y and p1rightHitbox > power4_x and chamaeleon == True and turn % 2 == 1:
            timea += 7
            chamaeleon = False
        if p2upHitbox < power4_y and p2leftHitbox < power4_x and p2downHitbox > power4_y and p2rightHitbox > power4_x and chamaeleon == True and turn % 2 == 0:
            timea += 7
            chamaeleon = False
        if p1upHitbox < p2downHitbox and p1leftHitbox < p2rightHitbox and p1downHitbox > p2upHitbox and p1rightHitbox > p2leftHitbox and freeze_time_start == False:
            variable = True
            turn += 1
            no_catch_time = timea
            freeze_time_start = True

            print('Da Hail')

        if freeze_time_start == True:
            if timea == no_catch_time - 2:
                freeze_time_start = False

        sec += 1
        if sec == 60:
            sec = 0
            timea -= 1

            # flip() the display to put your work on screen

        if tai_lung == False and timea != freeze_time - 2 and timea > freeze_time - 2:
            if a == False:
                player2_pos.x = freeze_pos_x
                player2_pos.y = freeze_pos_y
            else:
                player_pos.x = freeze2_pos_x
                player_pos.y = freeze2_pos_y

        pygame.display.flip()
        clock.tick(60)
pygame.quit()
