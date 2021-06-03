from zombie.core import Zombie,ZombieBehaviour

@Zombie.bind_script(script_name="MyScript",init_props=["gameObject","transform"])
class Myscript(ZombieBehaviour):
    def __init__(self):
        self.gameObject=None
        self.transform=None
    def on_update(self):
        print("Updating zombie")

@Zombie.bind_script(script_name='Enemy',init_props=[])
class Player(ZombieBehaviour):
    pass
