class Component:
    def __init__(self, data):
        self.__data = data

    def get(self):
        return self.__data


class MaterialComponent(Component):
    def __init__(self, material):
        super().__init__(material)


class RenderComponent(Component):
    def __init__(self, renderer):
        super().__init__(renderer)


class TransformCompnent(Component):
    def __init__(self, transform):
        super().__init__(transform)


class ColliderComponent(Component):
    def __init__(self, collider):
        super().__init__(collider)


class ScriptComponet(Component):
    def __init__(self, script):
        super().__init__(script)


class AnimationComponent(Component):
    def __init__(self, animation):
        super().__init__(animation)
