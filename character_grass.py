from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
while x < 780:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    x += 2
    delay(0.01)
    update_canvas()
while y < 560:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    y += 2
    delay(0.01)
    update_canvas()
while x > 10:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    x -= 2
    delay(0.01)
    update_canvas()
while y > 90:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    y -= 2
    delay(0.01)
    update_canvas()
while x <400:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    x += 2
    delay(0.01)
    update_canvas()

for i in range(-90, -90 - 360, -1):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    x=400 + 240 * math.cos(math.radians(i))
    y=330 + 240 * math.sin(math.radians(i))
    delay(0.01)
    update_canvas()

close_canvas()