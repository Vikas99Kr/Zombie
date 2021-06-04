# from zombie.core import ZombieSystem,GameView,Input
# ZombieSystem.init()
# display=GameView(600,500,"MyGame")
# def render(screen):
#     if Input.get_key_down('enter'):
#         print("Going Up")
#     elif Input.get_key_up('nenter'):
#         print("Some")
# display.run(render)
# ZombieSystem.quit()



from zombie.entity import Entity
from zombie.material import TextureMaterial,Material
from zombie.asset import AssetManager
from zombie.script import ScriptManager
ScriptManager.require_import(['zombie_test.zombies.actions'])
AssetManager.load_asset()
entity=Entity(_name="Square")
material:Material=TextureMaterial(image=AssetManager.get_asset("icon"))
entity.put_component('material',material)
print(entity)
print(ScriptManager.behaviours)
