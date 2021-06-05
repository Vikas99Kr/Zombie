from zombie.core import ZombieSystem, GameView, Input

ZombieSystem.init()
display = GameView(600, 500, "MyGame")


def render(screen):
    if Input.get_key_pressed('enter'):
        print("You pressed enter")
    if Input.get_mouse_button_down(0):
        print("Left Mouse Button is down")
    if Input.get_mosue_button_up(0):
        print("Left Mouse Button is released")
    if Input.get_mouse_button_down(2):
        print("Right mouse button is down")
    if Input.get_mosue_button_up(2):
        print("Right Mouse button is released")



display.run(render)
ZombieSystem.quit()