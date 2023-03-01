import play
import pygame

play.set_backdrop('light blue')
sounds = []
keys = []
controls = ["q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v", "b"]
print(len(controls))
octaves = ["", "f", "g"]
for i in range(3):

    for j in range(8):
        newKey = play.new_box(color="grey", width=20, height=80, x = -295 + j*25 + i*40 +i*160)
        keys.append(newKey)
        sounds.append(pygame.mixer.Sound(octaves[i] + str(j+1)+'.ogg'))
    

@play.when_program_starts
def start():
    pygame.mixer_music.load('./hello.mp3')
    pygame.mixer_music.play()

@play.repeat_forever
async def play_piano():
    for i in range(len(keys)):
        if keys[i].is_clicked or (play.key_is_pressed(controls[i])):
            keys[i].color = "white"
            sounds[i].play()
            await play.timer(seconds=0.3)
            keys[i].color = "grey"

play.start_program()