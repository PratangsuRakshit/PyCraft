import platform
from ursina import *
from random import randint
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from ursina.shaders import basic_lighting_shader
from ursina.shaders import lit_with_shadows_shader

shader = basic_lighting_shader
osv = (platform.release())
winos = (platform.system())
winost = winos+osv

class BGinv(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.720, 0.430),
            position=Vec2(0, 0),
            color=color.rgba(0, 0, 0.75, 100),
        )

class BG(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.465, 0.065),
            position=Vec2(0, -0.465),
            color=color.rgba(0, 0, 0.75, 100),
        )


class Underlay(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.46, 0.06),
            position=Vec2(0, -0.465),
            color=color.rgba(0, 0, 0.75, 100),
            texture=load_texture('assets/inventory underlay.png'))


class Inventory(Entity):
    def __init__(self, texture, position, letter):
        super().__init__(
            parent=camera.ui,
            scale=(0.05, 0.05),
            model='quad',
            position=position,
            texture=texture
        )
        self.letter = letter

    def input(self, key):
        if key == f"{self.letter}":
            self.scale = 0.06
        else:
            self.scale = 0.05

app = Ursina()

bg = BG()
bginv = BGinv()
vid =Entity(model='quad', position = Vec2(0,0),scale = (1.779,1),parent = camera.ui,texture = 'devjang intro.mp4',)
destroy(vid, delay=5)
underlay = Underlay()
inv1 = Inventory(load_texture('assets/grassinv1'), Vec2(-0.2, -0.465), '1')
inv2 = Inventory(load_texture('assets/dirtinv1'), Vec2(-0.15, -0.465), '2')
inv3 = Inventory(load_texture('assets/cobbleinv1'), Vec2(-0.10, -0.465), '3')
inv4 = Inventory(load_texture('assets/stoneinv1'), Vec2(-0.05, -0.465), '4')
inv5 = Inventory(load_texture('assets/loginv1'), Vec2(0, -0.465), '5')
inv6 = Inventory(load_texture('assets/leafinv1'), Vec2(0.05, -0.465), '6')
inv7 = Inventory(load_texture('assets/coalinv1.png'), Vec2(0.10, -0.465), '7')
inv8 = Inventory(load_texture('assets/sandinv1.png'),Vec2(0.15, -0.465), '8')
inv9 = Inventory(load_texture('assets/glassinv1.png'),Vec2(0.20, -0.465), '9')
coal_oar_texture = load_texture('assets/coaltexture.png')
log_texture = load_texture('assets/logtexture.png')
stone_texture = load_texture('assets/stonetexture.png')
brick_texture = load_texture('assets/cobblestone.png')
dirt_texture = load_texture('assets/dirttexture.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
leaf_texture = load_texture('assets/leafblock.png')
sand_texture = load_texture('assets/sandtexture.png')
glass_texture = load_texture('assets/glasstexture.png')
grass_texture = load_texture('assets/grasstexture.png')
a = Audio('assets/Minecraft Footsteps.mp3', autoplay=False, loop=True)
seeder = randint(1, 18446744073709551616)
block_pick = 1
noise = PerlinNoise(octaves=1, seed=seeder)
xpix, ypix = 100, 100
pic = [[noise([i / xpix, j / ypix]) for j in range(xpix)] for i in range(ypix)]

window.fps_counter.enabled = True
window.exit_button.visible = False
window.fullscreen = False
window.icon = 'assets\pycrafticonimg.ico'
window.vsync = False

steve = Entity(model = load_model('assets/steve.obj'),texture = load_texture('assets/Steve.png'),scale = 0.2,rotation = (0,90,0))
steve.shader = False



def update():
    global block_pick
    global shader
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
    if held_keys['7']: block_pick = 7
    if held_keys['8']: block_pick = 8
    if held_keys['9']: block_pick = 9
    ppos = f'x = {round(player.x)}, y = {round(player.y)}, z = {round(player.z)}'
    player_pos_txt.text = str(ppos)
    if winost == 'Windows10':
        shader = lit_with_shadows_shader
    if winost == 'Windows11':
        shader = lit_with_shadows_shader

player = FirstPersonController(model = steve,jump_height = 1,)

player_pos_txt = Text(text='' , scale = 0.7,)
player_pos_txt.position = (-0.87,0.485)
player_pos_txt.font = 'assets/pix-pixelfjverdana12pt.regular.ttf'

def input(key):
    if held_keys['a'] or held_keys['w'] or held_keys['s'] or held_keys['d']:
        a.play()
    else:
        a.stop()


class Voxel(Button):
    def __init__(self, position=(0, 0, 1), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/blockk',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=1,
            shader = shader,
            mesh='triangle'
        )

        self.IsDestractable = True

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
                if block_pick == 1:
                    voxel.texture = grass_texture
                if block_pick == 2:
                    voxel.texture = dirt_texture
                if block_pick == 3:
                    voxel.texture = brick_texture
                if block_pick == 4:
                    voxel.texture = stone_texture
                if block_pick == 5:
                    voxel.texture = log_texture
                if block_pick == 6:
                    voxel.texture = leaf_texture
                if block_pick == 7:
                    voxel.texture = coal_oar_texture
                if block_pick == 8:
                    voxel.texture = sand_texture
                if block_pick == 9:
                    voxel.texture = glass_texture

            if self.IsDestractable != False:
                if key == 'right mouse down':
                    destroy(self)
            if held_keys['f']:
                window.fullscreen = not window.fullscreen
            if held_keys['e']:
                bginv.visible = not bginv.visible
            if key == 'right mouse down':
                destroy(self)
            if held_keys['tab']:
                camera.z = -5.5 if camera.z == 0.5 else 0.5
            if held_keys['tab']:
                steve.visible = True if steve.visible == False else False
            if held_keys['enter']:
                 player.speed = 3.5 if player.speed == 6.5 else 6.5

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='arm.obj',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.7, -0.6),
            shader = shader)

    def active(self):
        self.position = Vec2(0.6, -0.5)

    def passive(self):
        self.position = Vec2(0.7, -0.6)


for z in range(20):
    for x in range(20):
        y = noise([x / 8, z / 8])
        y = math.floor(y * 7.5)
        Voxel(position=(x, y, z))

        y = noise([x / 8, z / 8])
        y = math.floor(y * 7.5)
        Voxel(texture=dirt_texture, position=(x, (-1) + y, z))

        tree_chance = randint(1, randint(100, 150))
        if tree_chance == 5:
            tree_height = randint(3, 6)
            leaf_height = randint(1, 2)
            for y1 in range(tree_height):
                Voxel(texture=log_texture, position=(x, y1 + 1 + y, z))
            for y2 in range(leaf_height):
                Voxel(texture=leaf_texture, position=(x, y2 + tree_height + y + 2, z))
                for x1 in range(3):
                    for z1 in range(3):
                        Voxel(texture=leaf_texture, position=(x + x1 - 1, y2 + tree_height + y + 1, z + z1 - 1))

for z in range(20):
    for x in range(20):
        for y1 in range(3):
            y = noise([x / 8, z / 8])
            y = math.floor(y * 7.5)
            Voxel(texture=stone_texture, position=(x, y - 4 + y1, z))


Sky(texture=sky_texture,shader = False)
hand = Hand()
pivot = Entity()
sun = DirectionalLight(rotation=(45,45,45))
print("@2021Copyright @DevjangStudios")
print('This Worlds seed was = ', seeder, )

app.run()
