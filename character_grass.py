from pico2d import *
import math

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400, 30)
character.draw_now(400, 90)
delay(1)



def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.1)



def run_circle():
    print('CIRCLE')
    cx, cy, r = 400, 300, 210
    
    for deg in range(-90, 270, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        render_frame(x, y)
        


def run_rectangle():
    print('RECTANGLE')

    # right
    for x in range(400, 750 + 1, 10):
        render_frame(x, 90) # 해당 좌표에 캐릭터 그리기

    # up
    for y in range(90, 550 + 1, 10):
        render_frame(750, y)


    
while True:
    # run_circle()
    run_rectangle()
    break



close_canvas()
