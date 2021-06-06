from zombie.material import TextureMaterial
from zombie.physics import Transform
class Component:
    def __init__(self, data,entity):
        self.__data = data
        self.__entity=entity

    def get(self):
        return self.__data
    def set(self,data):
        self.__data=data
    def get_p(self):
        return self.__entity


class SpriteRenderer(Component):
    def __init__(self, sprite:TextureMaterial,parent=None):
        super().__init__(sprite,parent)

class TransformComponent(Component):
    def __init__(self, transform:Transform,parent=None):
        super().__init__(transform,parent)

class ColliderComponent(Component):
    def __init__(self, collider,parent=None):
        super().__init__(collider,parent)


class ScriptComponent(Component):
    def __init__(self, script,parent=None):
        super().__init__(script,parent)


class AnimationComponent(Component):
    def __init__(self, animation,parent=None):
        super().__init__(animation,parent)

class ModelComponent(Component):
    def __init__(self,model,parent=None):
        super().__init__(model,parent)
