from random import randint
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from classes import *
# Please NOTE : inv1 = hotbar inventory and inv2 = inventory overall 
class BG(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (0.465,0.065),
            position = Vec2(0,-0.465),
            color = color.rgba(0, 0, 0.75,100),
            )
class Underlay(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (0.46,0.06),
            position = Vec2(0,-0.465),
            color = color.rgba(0, 0, 0.75,100),
            texture = load_texture('Minecraft-in-Python-main/assets/inventory underlay.png'))

class Inv1(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            scale = (0.05,0.05),
            model = 'quad',
            position = Vec2(-0.2,-0.465),
            texture = load_texture('Minecraft-in-Python-main/assets/grassinv1.png')
        )

    def input(self, key):
        if key == "1":
            self.scale = 0.06
        else:
            self.scale = 0.05


class Inv2(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            scale=(0.05, 0.05),
            model='quad',
            position= Vec2(-0.15, -0.465),
            texture=load_texture('Minecraft-in-Python-main/assets/stoneinv1.png')
            )

    def input(self, key):
        if key == "2":
            self.scale = 0.06
        else:
            self.scale = 0.05

class Inv3(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            scale=(0.05, 0.05),
            model='quad',
            position= Vec2(-0.10, -0.465),
            texture=load_texture('Minecraft-in-Python-main/assets/cobbleinv1.png')
            )

    def input(self, key):
        if key == "3":
            self.scale = 0.06
        else:
            self.scale = 0.05

class Inv4(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            scale=(0.05, 0.05),
            model='quad',
            position= Vec2(-0.05, -0.465),
            texture=load_texture('Minecraft-in-Python-main/assets/dirtinv1.png')
            )

    def input(self, key):
        if key == "4":
            self.scale = 0.06
        else:
            self.scale = 0.05
class Inv5(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            scale=(0.05, 0.05),
            model='quad',
            position= Vec2(0, -0.465),
            texture=load_texture('Minecraft-in-Python-main/assets/loginv1.png')
            )

    def input(self, key):
        if key == "5":
            self.scale = 0.06
        else:
            self.scale = 0.05
class Inv6(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            scale=(0.05, 0.05),
            model='quad',
            position= Vec2(0, -0.465),
            texture=load_texture('Minecraft-in-Python-main/assets/leafinv1.png')
            )
    def input(self, key):
        if key == "6":
            self.scale = 0.06
        else:
            self.scale = 0.05
app = Ursina()
bg = BG()
underlay = Underlay()
inv1 = Inv1()
inv2 = Inv2()
inv3 = Inv3()
inv4 = Inv4()
inv5 = Inv5()
inv6 = Inv6()
log_texture = load_texture('assets/log_texture.png')
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
leaf_texture = load_texture('assets/leaf_block.png')
a = Audio('assets/Minecraft Footsteps.mp4') #pragatsu change the path here<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
block_pick = 1
noise = PerlinNoise(octaves=1, seed=randint(1,18446744073709551616))
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

window.fps_counter.enabled = True
window.exit_button.visible = False
window.fullscreen = False
def update():

    global block_pick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
def input(key):
    if held_keys['a'] or held_keys['w'] or held_keys['s'] or held_keys['d']:
        a.play(start=0)
    else:
        a.stop()
        
for z in range(20):
    for x in range(20):
                y = noise([x/8,z/8])
                y =math.floor(y * 7.5)
                Voxel(position=(x, y, z))

                y = noise([x / 8, z / 8])
                y = math.floor(y * 7.5)
                Voxel(texture=dirt_texture ,position=(x ,(-1) + y ,z))

                tree_chance = randint(1, randint(100, 130))
                if tree_chance == 5:
                    tree_height = randint(3, 6)
                    leaf_height = randint(1, 2)
                    for y1 in range(tree_height):
                        Voxel(texture=log_texture, position=(x, y1+1+y, z))
                    for y2 in range(leaf_height):
                        Voxel(texture=leaf_texture, position=(x, y2 + tree_height + y + 2, z))
                        for x1 in range(3):
                            for z1 in range(3):
                                Voxel(texture=leaf_texture, position=(x + x1 - 1, y2 + tree_height + y + 1, z+z1 - 1))

for z in range(20):
        for x in range(20):
            for y1 in range(3):
                y = noise([x / 8, z / 8])
                y = math.floor(y * 7.5)
                Voxel(texture=stone_texture ,position=(x ,y-4+y1 ,z))


player = FirstPersonController(jump_height=1)
player.position = Vec3(5, 5, 5)
Sky(texture = sky_texture,shader = False)
hand = Hand()
pivot = Entity()
PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))
app.run()
