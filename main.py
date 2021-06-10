from zombie.core import ZombieSystem, GameView
from zombie.scene import Scene
from zombie.entity import Entity
from zombie.components import SpriteRenderer,ScriptComponent
from zombie.script import ScriptManager
from zombie.material import TextureMaterial
from zombie.asset import AssetManager
rendering=True
ZombieSystem.init()
display = GameView(600, 500, "MyGame")
ScriptManager.require_import(list_packages=[
    'zombie_test.zombies.actions'
])


entity=Entity("ASLDKJF",None)
enemy=Entity('Enemy',None)
AssetManager.load_asset()
entity.put_component('renderer',SpriteRenderer(TextureMaterial(AssetManager.get_asset('aeroplane'),(80,80))))
entity.put_component('script',ScriptComponent('player'))

enemy.put_component('renderer',SpriteRenderer(TextureMaterial(AssetManager.get_asset('icon'),(80,80))))
enemy.put_component('script',ScriptComponent('enemy'))


scene:Scene=Scene([entity,enemy],None,display.screen)
display.run(scene)
rendering=False
ZombieSystem.quit()