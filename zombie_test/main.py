from zombie.core import GameObject,Zombie
from  zombie.material import TextureMaterial

gameObject=GameObject("MyObject")
gameObject.put_property('material',TextureMaterial())
gameObject.put_property('script','MyScript')
gameObject.get_property('material').get_material()
print(gameObject)

zombie=Zombie()
zombie.init_system()
zombie.import_script_packages(scripts=[
    "zombie_test.behaviours.beahviours"
])
print(Zombie.mapped_beahviour)
zombie.attach_everything(gameObject)