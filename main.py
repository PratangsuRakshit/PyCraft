from random import randint
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise

app = Ursina()
log_texture = load_texture('assets/log_texture.png')
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
block_pick = 1
noise = PerlinNoise(octaves=1, seed=randint(1,18446744073709551616))
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

window.fps_counter.enabled = True
window.exit_button.visible = False
window.fullscreen = True
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

class Voxel(Button):
    def __init__(self,position=(0,0,1),texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0 ,0 ,random.uniform(0.9 ,1)),
            scale=0.5,
            )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3:
                    voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4:
                    voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 5:
                    voxel = Voxel(position=self.position + mouse.normal, texture=log_texture)

            if key == 'right mouse down':
                destroy(self)

            if held_keys['escape']:
                window.fullscreen = False
            if held_keys['f']:
                window.fullscreen = True

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='arm.obj',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150 ,-10 ,0),
            position=Vec2(0.7,-0.6),
            )

    def active(self):
        self.position = Vec2(0.6, -0.5)

    def passive(self):
        self.position = Vec2(0.7, -0.6)

for z in range(20):
    for x in range(20):
                y = noise([x/8,z/8])
                y =math.floor(y * 7.5)
                voxel = Voxel(position=(x, y, z))
for z in range(20):
    for x in range(20):
                y = noise([x / 8, z / 8])
                y = math.floor(y * 7.5)
                voxel = Voxel(texture=dirt_texture ,position=(x ,(-1) + y ,z))
for z in range(20):
    for x in range(20):
                y = noise([x / 8, z / 8])
                y = math.floor(y * 7.5)
                voxel = Voxel(texture=stone_texture ,position=(x ,(-2) + y ,z))
for z in range(20):
    for x in range(20):
                y = noise([x / 8, z / 8])
                y = math.floor(y * 7.5)
                voxel = Voxel(texture=stone_texture ,position=(x ,(-3) + y ,z))
for z in range(20):
    for x in range(20):
                y = noise([x / 8, z / 8])
                y = math.floor(y * 7.5)
                voxel = Voxel(texture=stone_texture ,position=(x ,(-4) + y ,z))

player = FirstPersonController()
player.position = Vec3(5, 30, 5)
Sky(texture = sky_texture,shader = False)
hand = Hand()
pivot = Entity()
PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))
app.run()
