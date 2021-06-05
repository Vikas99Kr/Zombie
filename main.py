from zombie.core import ZombieSystem, GameView, Input

ZombieSystem.init()
display = GameView(600, 500, "MyGame")


def render(screen):
    if Input.get_key_pressed('enter'):
        print("You pressed enter")


display.run(render)
ZombieSystem.quit()