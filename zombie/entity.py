class Entity:
    def __init__(self, _name, _parent=None):
        self._children = []
        self._parent = _parent
        self._name = _name
        self._component = {
            "renderer": None,  # Rendering System
            "transform": None,
            "collider": None,  # Physics system
            "script": None,
            "material": None,  # Rendering System
            "animation": None,  # Animation System
        }

    def put_component(self, prop, comp):
        self._component[prop] = comp

    def get_component(self, prop):
        return self._component[prop]

    def __repr__(self):
        build: str = ""
        for i in self._component:
            build += f"{i} : {self._component[i]}\n"
        return build


class Camera(Entity):
    def __init__(self, _name, _parent):
        super().__init__(_name=_name, _parent=_parent)
