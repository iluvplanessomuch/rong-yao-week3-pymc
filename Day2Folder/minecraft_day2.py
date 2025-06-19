# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER



def on_chat():
    agent.teleport_to_player()
    
player.on_chat("fart", on_chat)


def turnleft(steps):
    agent.turn(LEFT)
    
player.on_chat("LEFT", turnleft)
def turnright():
        agent.turn(RIGHT)
player.on_chat("RIGHT", turnright)


def movef(steps):
    agent.move(FORWARD,steps)
player.on_chat("fore", movef)
def moveb(steps):
        agent.move(BACK,steps)
player.on_chat("back", moveb)
def moveu(steps):
    agent.move(UP,steps)
player.on_chat("up", moveu)
def moved(steps):
    agent.move(DOWN,steps)
player.on_chat("down", moved)

def on_chat2():
    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
def obby2():
    agent.turn(TurnDirection.LEFT)
    agent.turn(TurnDirection.LEFT)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 98765)
    agent.turn(TurnDirection.LEFT)
    agent.move(FORWARD, 141251235135)
    agent.turn(RIGHT)
    agent.move(FORWARD, 4)



player.on_chat("obby2", obby2)

def on_chat3():
    mobs.apply_effect(HEALTH_BOOST, mobs.target(NEAREST_PLAYER), 10, 1)
player.on_chat("food", on_chat3)


def choppy(height):
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    for count in range(height):
        agent.destroy(UP)
        agent.move(UP, 1)
player.on_chat("chop", choppy)

def cobbly(length):
    for count in range(length):

        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.move(FORWARD, 1)

player.on_chat("cobble", cobbly)
def on_chat4(turnaround):
    agent.turn(TurnDirection.LEFT)
    agent.turn(TurnDirection.LEFT)
player.on_chat("turnaround", on_chat4)

def bobthebuilder():
    for count in range(30):
        agent.place(UP)
        agent.place(DOWN)
        
        agent.move(BACK, 1)
        agent.place(FORWARD)

player.on_chat("bbb", bobthebuilder)








