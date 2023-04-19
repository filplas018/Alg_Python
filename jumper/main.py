import play 

play.set_backdrop('light blue')
tonda = play.new_circle(color = "green", radius=30, x=-300, y=-240)
deaths = 0
deathsText = play.new_text(color="red", font_size=35, words=str(deaths), x=250, y=250)
deadLine = play.new_box(color="light green", height=20, width=800, y = -300)
finish = play.new_circle(color="yellow", radius=15, x=100, y = 40)
winnerText = play.new_text(color="green", font_size=50, words="Vyhráls")
gameOver = play.new_text(color="red", font_size=50, words="Prohráls!")



level1 = [
    play.new_box(color="red", height=25, width=150, x=-300, y=-270),
    play.new_box(color="red", height=25, width=150, x=-120, y=-250),
    play.new_box(color="red", height=25, width=150, x=100, y=-200),
    play.new_box(color="red", height=25, width=150, x=300, y=-130),
    play.new_box(color="red", height=25, width=150, x=100, y=-70)]
level2 = [
    play.new_box(color="green", height=25, width=150, x=-300, y=200),
    play.new_box(color="green", height=25, width=150, x=-120, y=150),
    play.new_box(color="green", height=25, width=150, x=100, y=100),
    play.new_box(color="green", height=25, width=150, x=300, y=0),
    play.new_box(color="green", height=25, width=150, x=100, y=-130)]
level3 = [
    play.new_box(color="blue", height=25, width=150, x=-300, y=-300),
    play.new_box(color="blue", height=25, width=150, x=-120, y=-250),
    play.new_box(color="blue", height=25, width=150, x=100, y=-200),
    play.new_box(color="blue", height=25, width=150, x=300, y=-100),
    play.new_box(color="blue", height=25, width=150, x=100, y=30)]

levels = [level1, level2, level3]

actualLevel = 0

def jump():
    for i in level1:
        if(tonda.is_touching(i)):
            for i in range(1,80):
                tonda.y+=1
def activatePlatforms(level):
    for i in level:
        i.start_physics(can_move=False)

def hideLevels(levels):
    for i in levels:
        i.hide()

def showLevels(levels):
    for i in levels:
        i.show()

def changeLevel(currentLevel):
    global actualLevel
    hideLevels(levels[currentLevel])
    showLevels(levels[currentLevel+1])
    activatePlatforms(levels[currentLevel+1])
    winnerText.hide()
    actualLevel+=1
    newLevel = levels[actualLevel]

    finish.x = newLevel[len(newLevel)-1].x
    finish.y = newLevel[len(newLevel)-1].y + 30

    tonda.x = newLevel[0].x
    tonda.y = newLevel[0].y + 60

def resetLevel(currentLevel):
    
    level = levels[currentLevel]
    tonda.x = level[0].x
    tonda.y = level[0].y + 60
    
    

@play.when_program_starts
def start():

    tonda.start_physics(bounciness=0)
    activatePlatforms(level1)
    hideLevels(level2)
    hideLevels(level3)

    gameOver.hide()
    winnerText.hide()
    

@play.repeat_forever
async def do():
    global deaths
    if (play.key_is_pressed('w')):
        jump()
    if (play.key_is_pressed('a')):
        tonda.x -= 5
    if (play.key_is_pressed('d')):
        tonda.x += 5
    if(tonda.is_touching(finish)):
        winnerText.show()
        await play.timer(seconds=1.5)
        changeLevel(actualLevel)
    if(tonda.is_touching(deadLine)):
        gameOver.show()
        deaths+=1
        gameOver.show()
        await play.timer(seconds=1.5)
        gameOver.hide()
        resetLevel(actualLevel)
        deathsText.words = str(deaths)

play.start_program()