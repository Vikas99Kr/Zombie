import pygame
class Material:
    def __init__(self,material):
        self.material=material
    def get_material(self):
        return self.material

class TextureMaterial(Material):
    def __init__(self,image,size=()):
        self.__image=pygame.image.load(image)
        self.__nimage=image
        if size:
            self.__image=pygame.transform.scale(self.__image,(size[0],size[1]))
    def get_material(self):
        return self.__image
    def __repr__(self):
        return f"TextureMaterial(image:{self.__nimage},obj:{self.__image})"