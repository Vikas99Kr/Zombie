from zombie.physics import Transform,Vector2D,Scalar
from zombie.components import TransformComponent
class Entity:
    def __init__(self, _name, _parent=None):
        self.children = []
        self.parent = _parent
        self.name = _name
        self._component = {
            "renderer": None,  # Rendering System
            "transform": TransformComponent(Transform(Vector2D(0,0),Vector2D(1,1),Scalar(0))), #physics System
            "collider": None,  # Physics system
            "script": None,  # Scripting system
            "animation": None,  # Animation System
        }

    def put_component(self, prop, comp):
        self._component[prop] = comp

    def get_component(self, prop):
        return self._component[prop]
    def on_add(self):
        pass
    def on_remove(self):
        pass
    def __repr__(self):
        build: str = ""
        for i in self._component:
            build += f"{i} : {self._component[i]}\n"
        return build


class Camera(Entity):
    def __init__(self, _name, _parent):
        super().__init__(_name=_name, _parent=_parent)
