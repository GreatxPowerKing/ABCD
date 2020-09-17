from pico2d import *

open_canvas()
img = load_image('C:/Users/user/Desktop/2주차/character.png')
gra = load_image('C:/Users/user/Desktop/2주차/grass.png')

gra.draw_now(400, 30)

for x in range(0, 800, 5):
    #렌더링
    clear_canvas_now()
    gra.draw_now(400, 30)
    img.draw_now(x, 80)
    update_canvas()
    #
    #로직
    get_events()
    delay(0.01)
    #

delay(5)
close_canvas()





#RUN ANIMATION
open_canvas()
img = load_image('C:/Users/user/Desktop/2주차/run_animation.png')
gra = load_image('C:/Users/user/Desktop/2주차/grass.png')

gra.draw_now(400, 30)

frame = 0
for x in range(0, 800, 5):
    clear_canvas()
    gra.draw(400, 30)
    img.clip_draw(frame, 0, 100, 100, x, 80)
    update_canvas()
    frame = (frame + 1) % 8
    # = frame += 1
    #   if frame < 8: frame = 0
    get_events()
    delay(0.01)

delay(5)
close_canvas()
