from zombie.physics import Transform,Vector2D,Scalar
from zombie.components import SpriteRenderer,TransformComponent,ScriptComponent
from zombie.script import ScriptManager
from zombie.core import GameView
import threading
class Scene:
    def __init__(self, children=[], camera=None,screen=None):
        self._children = children
        self.camera = camera
        self.thread_list=[]
        self.screen=screen
        for child in children:
            scr:ScriptComponent=child.get_component('script')
            if scr:
                obj=ScriptManager.behaviours[scr.script].get_instance(child)
                obj.on_start()
                t1=threading.Thread(target=Scene.start_thread,args=(obj,))
                self.thread_list.append(t1)
                t1.start()
    @staticmethod
    def start_thread(obj):
        while GameView.running:
            obj.on_update()
            GameView.clock.tick(GameView.FPS)
    def on_update(self):
        for child in self._children:
            tx:TransformComponent=child.get_component('transform')
            tx:Transform=tx.transform
            renderer:SpriteRenderer=child.get_component('renderer')
            if  renderer:
                self.screen.blit(renderer.sprite.get_material(),(tx.translate.data[0],tx.translate.data[1]))

class SceneManager:
    __scenes = {}
    __current = None

    @staticmethod
    def get_current():
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
