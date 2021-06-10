class Zombie:
    def __init__(self):
        pass

    def on_start(self):
        pass

    def on_update(self):
        pass

    def on_collide(self, other):
        pass

class Script:
    def __init__(self, name):
        self.name = name
        self.instance=None

    def get_instance(self, game_object):
        if not self.instance:
            obj=self.name()
            obj.__dict__.update({"game_object": game_object})
            return obj
        return self.instance

    def __repr__(self):
        return str(self.name)


class ScriptManager:
    behaviours = {}

    @staticmethod
    def require_import(list_packages=[]):
        for pkg in list_packages:
            exec(f'import {pkg}')
            pass

    @staticmethod
    def bind(name):
        def myscript(scr):
            ScriptManager.behaviours.update({name: Script(scr)})
        return myscript
