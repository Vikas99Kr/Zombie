from zombie.script import ScriptManager, Zombie


@ScriptManager.bind(name="player")
class Player(Zombie):
    def on_start(self):
        pass

    def on_update(self):
        pass

    def on_collide(self, other):
        pass


@ScriptManager.bind(name="enemy")
class Enemy(Zombie):
    def on_start(self):
        pass

    def on_update(self):
        pass

    def on_collide(self, other):
        pass
