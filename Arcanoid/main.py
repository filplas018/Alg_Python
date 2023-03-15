import play
import pygame

rocket = play.new_box(color='red', width=150, height=15, y=-270)
baloon = play.new_circle(color='black', radius=10)
hitboxes = []
scoreText = play.new_text(color='black', x=-200, y = -350)

for i in range(5):
    for j in range(10):
        hitbox = play.new_box(color='grey', width=80, height=20, x=-360 + j*82, y=290 - i*22)
        hitboxes.append(hitbox)

@play.when_program_starts
def start():
    baloon.start_physics(can_move=True, stable=False, y_speed=-100, x_speed=10, friction=0.0)
    rocket.start_physics(can_move=False)
    for i in range(50):
        hitboxes[i].start_physics(can_move=False)
    

@play.repeat_forever
def do():
    position = pygame.mouse.get_pos()[0] ## pozice kurzoru
    rocket.x = position - 400
    for i in range(len(hitboxes)-1):
        if(hitboxes[i].is_touching(baloon)): # pokud se balonek a hitbox dotkly -> otoč x směr (rychlost)
            hitboxes[i].hide()
            del hitboxes[i]

        #if pokud se balonek dotkne zeme -> konec -> reset


play.start_program()