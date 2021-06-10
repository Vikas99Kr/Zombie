from zombie.script import ScriptManager, Zombie


@ScriptManager.bind(name="player")
class Player(Zombie):
    def __init__(self):
        pass
    def on_start(self):
        pass

    def on_update(self):
        self.game_object.get_component('transform').transform.translate.data+=1
        pass

    def on_collide(self, other):
        pass


@ScriptManager.bind(name="enemy")
class Enemy(Zombie):
    def on_start(self):
        self.game_object.get_component('transform').transform.translate.data[0]=500
        pass

    def on_update(self):
        self.game_object.get_component('transform').transform.translate.data[0] -= 1
        self.game_object.get_component('transform').transform.translate.data[1] += 1
        pass

    def on_collide(self, other):
        pass
