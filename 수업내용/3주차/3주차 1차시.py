from pico2d import *

open_canvas()

img = load_image('C:/Users/user/Desktop/2주차/run_animation.png')
gra = load_image('C:/Users/user/Desktop/2주차/grass.png')

gra.draw_now(400, 30)

running = True
x = 0
frame = 0
while running and x < 800:
    clear_canvas()
    
    gra.draw(400, 30)
    img.clip_draw(frame * 100, 0, 100, 100, x, 80)
    
    update_canvas()
    
    frame = (frame + 1) % 8
    x += 2
    
    evts = get_events()
    for e in evts:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
                #이중 루프를 중지시킴
                
        
    delay(0.01)

delay(5)
close_canvas()
