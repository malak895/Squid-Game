from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen = True
window.color = color.black

music = Audio("C:\\Users\\Malek\\Desktop\\Innovaation_center\\API\\Scary Horror.mp3", loop=True)
music.play()

player = FirstPersonController(collider='box', jump_duration=0.35)
player.cursor.visible = False

ground = Entity(model='plane', texture='grass', collider='mesh', scale=(30, 0, 3))

pill1 = Entity(model='cube', color=color.hsv(0, 1, 1), scale=(0.4, 0.1, 53), z=28, x=-0.7)
pill2 = duplicate(pill1, x=-3.7)
pill3 = duplicate(pill1, x=0.6)
pill4 = duplicate(pill1, x=3.6)

from random import randint
blocks = []
for i in range(12):
    block = Entity(model='cube', collider='box', color=color.white33, position=(2, 0.1, 3 + i * 4), scale=(3, 0.1, 2.5))
    block2 = duplicate(block, x=-2.2)
    blocks.append((block, block2, randint(0, 10) > 7, randint(0, 10) > 7))

goal = Entity(color=color.brown, model='cube', z=55, scale=(10, 1, 10))
pillar = Entity(color=color.red, model='cube', z=58, scale=(1, 15, 1), y=8)

game_over_text = Text(
    text='Game Over',
    scale=2,
    position=(0, 0.2),
    background=True,
    background_color=color.black,
    color=color.white,
    enabled=False
)

def replay_game():
    # Reset game state here
    print('Game replayed')

    # Restart game music
    music.stop()
    music.play()

replay_button = Button(text='Replay', position=(-0.5, -0.5), scale=(0.1, 0.05))
replay_button.on_click = replay_game

def show_mouse_cursor():
    player.cursor.visible = True
    replay_button.text_entity.enabled = True

def hide_mouse_cursor():
    player.cursor.visible = False
    replay_button.text_entity.enabled = False

def update():
    for block1, block2, k, n in blocks:
        for x, y in [(block1, k), (block2, n)]:
            if x.intersects() and y:
                invoke(destroy, x, delay=0.1)
                x.fade_out(duration=0.1)

    if player.y < -10:  # Change this condition to your game over condition
        game_over_text.enabled = True
        invoke(show_mouse_cursor)
    else:
        game_over_text.enabled = False
        invoke(hide_mouse_cursor)

def input(key):
    if key == 'q':
        music.stop()
        quit()

app.run()
