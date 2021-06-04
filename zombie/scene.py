from zombie.entity import Entity, Camera


class Scene(Entity):
    def __init__(self, children=[], camera=None):
        self._children = children
        self.camera = camera


class SceneManager:
    __scenes = {}
    __current = None

    @staticmethod
    def get_current(scene_name):
        return SceneManager.__current

    @staticmethod
    def add_scene(scene_name: str, scene: Scene):
        SceneManager.__scenes.update({scene_name: scene})

    @staticmethod
    def change_scene(scene_name: str):
        SceneManager.__current = SceneManager.__scenes[scene_name]

    @staticmethod
    def change_scene_index(scene_index: int):
        for i, scene in enumerate(SceneManager.__scenes):
            if i == scene_index:
                SceneManager.__current = scene
                return scene_index
