from zombie.material import TextureMaterial
from zombie.physics import Transform
class Component:
    def __init__(self):
        pass


class SpriteRenderer(Component):
    def __init__(self, sprite:TextureMaterial):
        self.sprite=sprite

class TransformComponent(Component):
    def __init__(self, transform:Transform):
        self.transform=transform

class ColliderComponent(Component):
    def __init__(self, collider):
        self.collider=collider


class ScriptComponent(Component):
    def __init__(self, script):
        self.script=script


class AnimationComponent(Component):
    def __init__(self, animation,controller):
        self.animation=animation
        self.controller=controller

class ModelComponent(Component):
    def __init__(self,model):
        self.model=model
