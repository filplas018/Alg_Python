import play 
import random

automat = play.new_image(image="./sprites/automat.png", size=900)
number1 = 0
number2 = 0
number3 = 0
score = 0

num1 = play.new_text(words=str(number1),x=-75, y=75)
num2 = play.new_text(words=str(number2), x=0, y=75)
num3 = play.new_text(words=str(number3), x=75, y=75)
scoreText = play.new_text(words=str(score), x = 100, y = 200)
button = play.new_text(words="Go!", size=100, y=-70)

message = play.new_text(words="Good luck!")

def generateNumbers():
    global number1, number2, number3
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    number3 = random.randint(0,9)

@play.when_program_starts

def start():
    print()

@button.when_clicked
def do():
    generateNumbers()

@play.repeat_forever

def do():
    num1.words=str(number1)
    num2.words=str(number2)
    num3.words=str(number3)



play.start_program()