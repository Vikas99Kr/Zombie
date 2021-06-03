import pygame
class GameObject:
    def __init__(self,name):
        self.__properties={
            "transform":Transform((0,0),90,(1,1))
        }
        self.__name=name
        self.__children={}
        pass
    def set_script_property(self,prop,value):
        if self.get_property('script') is not None:
            self.get_property('script')
    def get_name(self):
        return self.__name
    def put_property(self,k,prop):
        self.__properties.update({k:prop})
    def get_property(self,k):
        return self.__properties[k]
    def __repr__(self):
        reprs:str=""
        for k,val in enumerate(self.__properties):
            reprs+=f"prop:{k}> {val} [ {self.__properties[val]} ]\n"
        return reprs
    def add_child(self,child):
        self.__children.update({child.get_name():child})
    def remove_child(self,name):
        self.__children.pop(name)

class Zombie:
    mapped_beahviour = {}
    def __init__(self):

        pass
    def init_system(self):
        pygame.init()
    @staticmethod
    def bind_script(script_name,init_props:list):
        def script_binder(clz):
            Zombie.mapped_beahviour.update({script_name:[clz,init_props]})
        return script_binder
    def import_script_packages(self,scripts=[]):
        for script in scripts:
            exec(f'import {script}')
    def attach_everything(self,gameObject:GameObject):
        script=gameObject.get_property('script')
        if script is not None:
            obj=Zombie.mapped_beahviour[script][0]()
            exec('obj.gameObject=obj')
            exec('obj.transform=gameObject.get_property("transform")')
            obj.on_update()


class ZombieBehaviour:
    def __init__(self):
        pass
    def on_update(self):
        pass
    def on_collision(self,other:GameObject):
        pass
    def on_fixed_update(self):
        pass

class Transform:
    def __init__(self,translate,rotate,scale):
        self._translate=translate
        self._rotate=rotate
        self._scale=scale
    def get_translate(self):
        return self._translate
    def set_translate(self,x,y):
        self._translate=(x,y)
