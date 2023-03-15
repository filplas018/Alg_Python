import play
import pygame

play.set_backdrop('light blue')
sounds = []
keys = []
controls = ["q","w","e","r","t","z","u","i"]
octaves = ["", "f", "g"]

def changeInstrument(ins):
    sounds = []
    for i in range(8):
        sounds.append(pygame.mixer.Sound( ins + str(i+1)+'.ogg'))
    print(len(sounds))

ch_p = play.new_circle(
        color='black', x=-180, y=-150, radius=10, 
        border_color='black', border_width=2)
txt_p = play.new_text(words='piano', x=-145, y=-150, font_size=20)
ch_g = play.new_circle(
        color='light blue', x=-80, y=-150, radius=10, 
        border_color='black', border_width=2)
txt_g = play.new_text(words='guitar', x=-45, y=-150, font_size=20)
ch_f = play.new_circle(
        color='light blue', x=120, y=-150, radius=10, 
        border_color='black', border_width=2)
txt_f = play.new_text(words='flute', x=155, y=-150, font_size=20)


for i in range(8):
    newKey = play.new_box(color="grey", width=20, height=80, x = -160 + i*25 + i*25)
    keys.append(newKey)
    sounds.append(pygame.mixer.Sound(str(i+1)+'.ogg'))
    

@play.when_program_starts
def start():
    ##changeInstrument("")
    pygame.mixer_music.load('./hello.mp3')
    ##pygame.mixer_music.play()

@play.repeat_forever
async def play_piano():
    for i in range(len(keys)):
        if keys[i].is_clicked or (play.key_is_pressed(controls[i])):
            keys[i].color = "white"
            print(len(sounds))
            print(i)
            sounds[i].play()
            await play.timer(seconds=0.3)
            keys[i].color = "grey"

@ch_p.when_clicked
async def doP():
    changeInstrument("")
@ch_f.when_clicked
async def doF():
    changeInstrument("f")
@ch_g.when_clicked
async def doG():
    changeInstrument("g")

play.start_program()