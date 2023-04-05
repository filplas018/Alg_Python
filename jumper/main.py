import play 


play.set_backdrop('light blue')
tonda = play.new_circle(color = "green", radius=30, x=-300, y=-240)

p1 = play.new_box(color="red", height=25, width=150, x=-300, y=-300)
p2 = play.new_box(color="red", height=25, width=150, x=-120, y=-250)
p3 = play.new_box(color="red", height=25, width=150, x=100, y=-200)
p4 = play.new_box(color="red", height=25, width=150, x=300, y=-100)
p5 = play.new_box(color="red", height=25, width=150, x=100, y=30)
finish = play.new_circle(color="yellow", radius=15, x=100, y = 87)
winnerText = play.new_text(color="green", font_size=50, words="Vyhráls")



@play.when_program_starts
def start():
    tonda.start_physics(bounciness=0)
    #activatePlatforms(level1)
    p1.start_physics(can_move=False)
    p2.start_physics(can_move=False)
    p3.start_physics(can_move=False)
    p4.start_physics(can_move=False)
    p5.start_physics(can_move=False)

    winnerText.hide()
    

@play.repeat_forever
async def do():
    if (play.key_is_pressed('w')):
        tonda.y += 10
    if (play.key_is_pressed('s')):
        tonda.y -= 10
    if (play.key_is_pressed('a')):
        tonda.x -= 10
    if (play.key_is_pressed('d')):
        tonda.x += 10
    if(tonda.is_touching(finish)):
        winnerText.show()

play.start_program()