import play 

@play.when_program_starts
def start():
    print()

@play.repeat_forever
def do():
    print()

play.start_program()