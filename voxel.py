from ursina import *

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
                    voxel.texture = stone_texture
                if block_pick == 4:
                    voxel.texture = log_texture
                if block_pick == 5:
                    voxel.texture = brick_texture
                if block_pick == 6:
                    voxel.texture = leaf_texture

            if self.IsDestractable != False:
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
