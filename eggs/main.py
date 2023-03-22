import play 
import random
score = 0
play.set_backdrop('light blue')
platform1 = play.new_box(color="blue", width=230, height=10, x=-300, y=200, angle=-25)
platform2 = play.new_box(color="blue", width=230, height=10, x=-300, y=100, angle=-25)
platform3 = play.new_box(color="blue", width=230, height=10, x=300, y=200, angle=205)
platform4 = play.new_box(color="blue", width=230, height=10, x=300, y =100, angle= 205)
redline = play.new_box(color="red", width=800, height=10, y= -300)
basket = play.new_image(image="./basket.png", size=200, y=-150)
egg = play.new_circle(color="white", radius=20)
fail = play.new_text(color='red', font_size=50, words="You failed!")
scoreText = play.new_text(font_size=38, x=100, y=100)

async def spawnEgg():
    randomPlace = random.randint(1,4)
    
    await play.timer(seconds=2)
    if randomPlace == 1:
        egg.go_to(x=-290, y =225)
    if randomPlace == 2:
        egg.go_to(x=290, y =125)
    if randomPlace == 3:
        egg.go_to(x=-290, y =225)
    if randomPlace == 4:
        egg.go_to(x=290, y =125)



@play.when_program_starts

def start():
    fail.hide()
    platform1.start_physics(can_move=False)
    platform2.start_physics(can_move=False)
    platform3.start_physics(can_move=False)
    platform4.start_physics(can_move=False)
    egg.start_physics(can_move=True, stable=False)
    redline.start_physics(can_move=False)

@play.repeat_forever
async def do():
    global score
    scoreText.words = str(score)
    await spawnEgg()
    if(play.key_is_pressed('w')):
        basket.y+=10
    if(play.key_is_pressed('s')):
        basket.y-=10
    if(play.key_is_pressed('a')):
        basket.x-=10
    if(play.key_is_pressed('d')):
        basket.x+=10
    if(egg.is_touching(basket)):
        score+=1
        
    if(egg.is_touching(redline)):
        fail.show()
        platform1.hide()
        platform2.hide()
        platform3.hide()
        platform4.hide()
        egg.hide()
        basket.hide()
    

play.start_program()