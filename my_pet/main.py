import play 

#config 
alien = play.new_image(image="./sprites/alien0.png", size=900)
greenFace = play.new_image(image="./sprites/smiles0.png", size=400, x=-300, y=220)
redFace = play.new_image(image="./sprites/smiles1.png", size=400, x=300, y = 220)

#dobry veci
q = play.new_text(words="Pohladit: Q", x=-300, y=160, font_size=20)
w = play.new_text(words="Najíst: W", x=-300, y = 120, font_size=20)
e = play.new_text(words="Vyvenčit: E", x=-300, y=80, font_size=20)
r = play.new_text(words="Dát hračku: R", x=-300, y=40, font_size=20)
t = play.new_text(words="Pustit pohádku: T", x=-300, y=0, font_size=20)

#spatny veci
a = play.new_text(words="Fouknout: A",x=300, y=160, font_size=20)
s = play.new_text(words="Sníst mu oběd: S",x=300, y=120, font_size=20)
d = play.new_text(words="Nevyvenčit: D",x=300, y=80, font_size=20)
f = play.new_text(words="Sebrat hračku: F",x=300, y=40, font_size=20)
g = play.new_text(words="Pustit horror: G",x=300, y=0, font_size=20)




happiness = 0
happinessText = play.new_text(words='0', x=100, y = 100)

def setFace(happiness):
    if(happiness > 100 and happiness < 200):
        alien.image = "./sprites/alien1.png"
    elif(happiness > 200 and happiness < 300):
        alien.image = "./sprites/alien2.png"
    elif(happiness > 300 and happiness < 400):
        alien.image = "./sprites/alien3.png"
    elif(happiness >= 400):
        alien.image = "./sprites/alien4.png"

@play.when_program_starts
def start():
    print()

@play.repeat_forever

def do():
    global happiness
    # dobry veci
    if play.key_is_pressed('q'):
        happiness +=1
        happinessText.words=str(happiness)
    if play.key_is_pressed('w'):
        happiness += 1
        happinessText.words=str(happiness)
    if play.key_is_pressed('e'):
        happiness += 1
        happinessText.words=str(happiness)
    if play.key_is_pressed('r'):
        happiness += 1
        happinessText.words=str(happiness)
    if play.key_is_pressed('t'):
        happiness += 1
        happinessText.words=str(happiness)
    
    #spatny veci
    if play.key_is_pressed('a'):
        happiness -=1
        happinessText.words=str(happiness)
    if play.key_is_pressed('s'):
        happiness -= 1
        happinessText.words=str(happiness)
    if play.key_is_pressed('d'):
        happiness -= 1
        happinessText.words=str(happiness)
    if play.key_is_pressed('f'):
        happiness -= 1
        happinessText.words=str(happiness)
    if play.key_is_pressed('g'):
        happiness -= 1
        happinessText.words=str(happiness)

    setFace(happiness)
        
    

play.start_program()