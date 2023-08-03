import pygame as pg
from button import Button
from coin_looper import CoinRotater
from helpers import get_screen_size
import settings
from sound import Sound

pg.init()

pg.mouse.set_visible(False)

screen = pg.display.set_mode(get_screen_size())

clock = pg.time.Clock()

background = pg.image.load("images/menu/start_screen.jpg").convert_alpha()
cursor = pg.image.load("images/cursor/cursor.png").convert_alpha()

quit_button = Button((100, 40, 0), (180, 180, 180), (350, 400, 220, 70))
quit_button.default_button_construction("Quit", "Georgia", 50, (255, 255, 255), True, True)
settings_button = Button((100, 40, 0), (180, 180, 180), (350, 250, 220, 70))
settings_button.default_button_construction("Start", "Georgia", 50, (255, 255, 255), True, True)
sound_on = pg.image.load("images/sound/sound_on.png").convert_alpha()
sound_off = pg.image.load("images/sound/sound_off.png").convert_alpha()
sound_button = Sound(800, 700, sound_on, sound_off)

pg.mixer.music.load('music/sound_of_menu/sound_for_menu.mp3')
pg.mixer.music.play()
pg.mixer.music.set_volume(settings.GAME_SOUND)


coin_images = [pg.image.load(f"images/coins/coin_{i}.png").convert_alpha() for i in range(10)]
coin_looper = CoinRotater(coin_x=10,
                          coin_y=10,
                          images=coin_images
                          )

game_running = True
while game_running:
    clock.tick(settings.GAME_FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            left_clicked = pg.mouse.get_pressed()[0]
            if left_clicked:
                sound_button.turn_off_on()
        elif event.type == pg.MOUSEBUTTONUP:
            pass

    screen.blit(background, (0, 0))

    coin_looper.rotate_coin(screen)

    mouse_position = pg.mouse.get_pos()

    settings_button.if_the_courser_is_above_the_button(mouse_position, screen)
    quit_button.if_the_courser_is_above_the_button(mouse_position, screen)

    sound_button.display_image(screen)

    screen.blit(cursor, mouse_position)
    pg.display.update()

pg.quit()
