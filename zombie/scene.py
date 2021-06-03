from zombie.core import GameObject
class Scene:
    def __init__(self,scene_name,root_object:GameObject):
        self.__scene_name=scene_name
        self.__root_object=root_object
    def get_name(self):
        return self.__scene_name
    def get_root(self):
        return self.__root_object
