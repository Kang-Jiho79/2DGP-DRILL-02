from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 402
y = 90
angle = -90

while True:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    if x == 400 and y == 90:
        x = 400 + 240 * math.cos(math.radians(angle))
        y = 330 + 240 * math.sin(math.radians(angle))
        angle -= 2
    elif x < 780 and y == 90:
        x += 2
    elif x == 780 and y < 560:
        y += 2
    elif x > 10 and y == 560:
        x -= 2
    elif x == 10 and y > 90:
        y -= 2
    else:
        x = 400 + 240 * math.cos(math.radians(angle))
        y = 330 + 240 * math.sin(math.radians(angle))
        angle -= 2
        if angle == -90 - 360:
            x = 402
            y = 90
            angle = -90
    delay(0.01)
    update_canvas()

close_canvas()