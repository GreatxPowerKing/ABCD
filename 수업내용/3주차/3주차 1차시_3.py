from pico2d import *

def handle_events():
    global running, dx
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT: 
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE: 
                running = False
            elif e.key == SDLK_LEFT:
                    dx -= 1
            elif e.key == SDLK_RIGHT:
                    dx += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                    dx += 1
            elif e.key == SDLK_RIGHT:
                    dx -= 1
                    
open_canvas()

img = load_image('C:/Users/user/Desktop/2주차/run_animation.png')
gra = load_image('C:/Users/user/Desktop/2주차/grass.png')

gra.draw_now(400, 30)

running = True
x = get_canvas_width() // 2
dx = 0
frame = 0
while running and x < 800:
    clear_canvas()
    
    gra.draw(400, 30)
    img.clip_draw(frame * 100, 0, 100, 100, x, 80)
    
    update_canvas()

    x += dx * 5
    frame = (frame + 1) % 8
    
    handle_events()        
        
    delay(0.01)

delay(5)
close_canvas()
