import play
import random
score = 0
play.set_backdrop('light blue')
platform1 = play.new_box(color="blue", width=230,
                         height=10, x=-300, y=200, angle=-25)
platform2 = play.new_box(color="blue", width=230,
                         height=10, x=-300, y=100, angle=-25)
platform3 = play.new_box(color="blue", width=230,
                         height=10, x=300, y=200, angle=205)
platform4 = play.new_box(color="blue", width=230,
                         height=10, x=300, y=100, angle=205)
redline = play.new_box(color="red", width=800, height=10, y=-300)
basket = play.new_image(image="./basket.png", size=200, y=-150)
egg = play.new_circle(color="white", radius=20)
fail = play.new_text(color='red', font_size=50, words="You failed!")
welcome = play.new_text(color='red', font_size=50,
                        words="Welcome to the egg catcher!")
scoreText = play.new_text(font_size=38, x=300, y=270)
newGameButton = play.new_text(
    font_size=64, color='green', y=-100, words="New Game")


def spawnEgg():
    randomPlace = random.randint(1, 4)

    if randomPlace == 1:
        egg.go_to(x=-290, y=225)
    if randomPlace == 2:
        egg.go_to(x=290, y=125)
    if randomPlace == 3:
        egg.go_to(x=-290, y=125)
    if randomPlace == 4:
        egg.go_to(x=290, y=225)


def gameOver():
    fail.show()
    newGameButton.show()
    platform1.hide()
    platform2.hide()
    platform3.hide()
    platform4.hide()
    egg.hide()
    basket.hide()


def startNewGame():
    fail.hide()
    welcome.hide()
    newGameButton.hide()
    platform1.show()
    platform2.show()
    platform3.show()
    platform4.show()
    egg.show()
    basket.show()
    spawnEgg()


@newGameButton.when_clicked
def buttonClick():
    startNewGame()
    platform1.start_physics(can_move=False)
    platform2.start_physics(can_move=False)
    platform3.start_physics(can_move=False)
    platform4.start_physics(can_move=False)
    egg.start_physics(can_move=True, stable=False, bounciness=0)
    redline.start_physics(can_move=False)
    basket.start_physics(can_move=True, stable=True)
    
@play.when_program_starts
def start():
    platform1.hide()
    platform2.hide()
    platform3.hide()
    platform4.hide()
    egg.hide()
    basket.hide()
    fail.hide()
    
@play.repeat_forever
def do():
    global score
    scoreText.words = str(score)

    if (play.key_is_pressed('w')):
        basket.y += 10
    if (play.key_is_pressed('s')):
        basket.y -= 10
    if (play.key_is_pressed('a')):
        basket.x -= 10
    if (play.key_is_pressed('d')):
        basket.x += 10
    if (egg.is_touching(basket)):
        score += 1
        spawnEgg()

    if (egg.is_touching(redline)):
        gameOver()


play.start_program()
