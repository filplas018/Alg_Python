import play
import random

welcomeText = play.new_text(words="Try to get 21 points and beat the computer!", y=240)

addCardButton = play.new_box(color="yellow", width=100, height=35, x=-100, y=-240)
addCardText = play.new_text(words="Add Card", x = -100, y = -240, font_size=24)

startChallengeButton = play.new_box(color="red", width=120, height=35, x=100, y=-240)
startChallengeText = play.new_text(words="Challenge me!", x = 100, y = -240, font_size=24)

playerWindow = play.new_box(color="light blue", width=190, height=270, x=-100, y=-70)
computerWindow = play.new_box(color="light blue", width=190, height=270, x=100, y=-70)

playerDraws = 0
computerDraws = 0
playerDrawsText = play.new_text(words="0", x=-210, y=-210)
computerDrawsText = play.new_text(words="0", x=210, y=-210) 


playerScore = 0
computerScore = 0
playerScoreText = play.new_text(words="0", x=-100, y=70)
computerScoreText = play.new_text(words="0", x=100, y=70)

playerAdd = 0
computerAdd = 0
playerAddText = play.new_text(words="0", x=-100, y=0)
computerAddText = play.new_text(words="0", x=100, y=0)


winnerText = play.new_text(words="You are the winner!", y = 100)
lostText = play.new_text(words="You lost the game! :(", y = 100)

def initGame():
    global playerScore, computerScore, playerDraws, computerDraws, playerAdd, computerAdd
    playerScore = 0
    playerScoreText.words = playerScore
    computerScore = 0
    computerScoreText.words = computerScore
    playerDraws = 0
    playerDrawsText.words = playerDraws
    computerDraws = 0
    computerDrawsText.words = computerDraws
    playerAdd = 0
    computerAdd = 0
    playerAddText.words = playerAdd
    computerAddText.words = computerAdd
    winnerText.hide()
    lostText.hide()

def addCardPlayer():
    global playerScore, playerDraws
    playerAdd = random.randint(1,10)
    playerAddText.words = str(playerAdd)
    playerScore += playerAdd
    playerScoreText.words = str(playerScore)
    playerDraws += 1
    playerDrawsText.words = str(playerDraws)

def addCardComputer():
    global computerScore, computerDraws
    computerAdd = random.randint(1,10)
    computerAddText.words = str(computerAdd)
    computerScore += computerAdd
    computerScoreText.words = str(computerScore)
    computerDraws += 1
    computerDrawsText.words = str(computerDraws)


@play.when_program_starts
def start():
    initGame()
@play.repeat_forever
def do():
    if((computerScore == 21 and computerScore > playerScore) or playerScore > 21):
        lostText.show()
    if((playerScore == 21 and playerScore > computerScore) or computerScore > 21): #pokud je playerScore menší než computerScore nebo playerScore je vyšší než 21
        winnerText.show()

@startChallengeButton.when_clicked
def startClickFunction():
    initGame()
@addCardButton.when_clicked
async def addClickFunction():
    addCardPlayer()
    await play.timer(seconds=2)
    addCardComputer()

play.start_program()