import math

import config
import entity.boxmodel
import globals as G
import imagecutter
import mathhelper

BODY_HEIGHT = 2.0 / 3.0
BODY_LENGTH = BODY_HEIGHT * (2.0 / 3.0)
BODY_WIDTH = BODY_LENGTH / 2
HEAD_LENGTH = BODY_LENGTH
HEAD_WIDTH = HEAD_LENGTH
HEAD_HEIGHT = HEAD_LENGTH
ARM_HEIGHT = BODY_HEIGHT
ARM_LENGTH = BODY_WIDTH
ARM_WIDTH = BODY_WIDTH
LEG_HEIGHT = BODY_HEIGHT
LEG_LENGTH = BODY_WIDTH
LEG_WIDTH = BODY_WIDTH

imagecutter.cut_image(
    G.local + "/assets/minecraft/textures/entity/steve.png",
    (0, 0),
    (64, 32),
    G.local + "/tmp/entity/steve.png",
)
imagecutter.cut_image(
    G.local + "/assets/minecraft/textures/entity/alex.png",
    (0, 0),
    (64, 32),
    G.local + "/tmp/entity/alex.png",
)
imagecutter.resize(G.local + "/tmp/entity/steve.png", (256, 128))
imagecutter.resize(G.local + "/tmp/entity/alex.png", (256, 128))


class PlayerEntity(G.entityclass):
    tags = ["player"]

    def __init__(self, position=(0, 0, 0)):
        G.entityclass.__init__(self, position)
        self.rotation = 0
        self.position = position
        self.player = G.player
        self.image = mathhelper.load_image(
            G.local + "/tmp/entity/" + ("steve.png" if config.SKIN == 0 else "alex.png")
        )
        # self.image = mathhelper.load_image(G.local+"/assets/minecraft/textures/entity/char.png")
        self.head = entity.boxmodel.BoxModel(
            HEAD_LENGTH, HEAD_WIDTH, HEAD_HEIGHT, self.image, 32, 32, 32
        )
        self.head.update_texture_data(
            [(32, 96), (64, 96), (0, 64), (64, 64), (32, 64), (96, 64)]
        )
        # body
        self.body = entity.boxmodel.BoxModel(
            BODY_LENGTH, BODY_WIDTH, BODY_HEIGHT, self.image, 32, 16, 48
        )
        self.body.update_texture_data(
            [(80, 48), (112, 48), (64, 0), (112, 0), (80, 0), (128, 0)]
        )
        # left/right arm
        self.left_arm = entity.boxmodel.BoxModel(
            ARM_LENGTH, ARM_WIDTH, ARM_HEIGHT, self.image, 16, 16, 48
        )
        self.left_arm.update_texture_data(
            [
                (176, 48),
                (176 + 16, 48),
                (176, 0),
                (176 + 32, 0),
                (176 - 16, 0),
                (176 + 16, 0),
            ]
        )
        self.right_arm = entity.boxmodel.BoxModel(
            ARM_LENGTH, ARM_WIDTH, ARM_HEIGHT, self.image, 16, 16, 48
        )
        self.right_arm.update_texture_data(
            [
                (176, 48),
                (176 + 16, 48),
                (176, 0),
                (176 + 32, 0),
                (176 - 16, 0),
                (176 + 16, 0),
            ]
        )
        # left/right leg
        self.left_leg = entity.boxmodel.BoxModel(
            LEG_LENGTH, LEG_WIDTH, LEG_HEIGHT, self.image, 16, 16, 48
        )
        self.left_leg.update_texture_data(
            [(16, 48), (16 + 16, 48), (0, 0), (32, 0), (16, 0), (48, 0)]
        )
        self.right_leg = entity.boxmodel.BoxModel(
            LEG_LENGTH, LEG_WIDTH, LEG_HEIGHT, self.image, 16, 16, 48
        )
        self.right_leg.update_texture_data(
            [(16, 48), (16 + 16, 48), (0, 0), (32, 0), (16, 0), (48, 0)]
        )

        self.update_position(position)

        self.boxmodels = [
            self.head,
            self.body,
            self.left_arm,
            self.right_arm,
            self.left_leg,
            self.right_leg,
        ]

    def update_position(self, position, init=False):
        self.position = position
        x, y, z = position
        foot_height = y - 1.25

        self.head.position = (
            x - HEAD_LENGTH / 2,
            foot_height + LEG_HEIGHT + BODY_HEIGHT,
            z - HEAD_WIDTH / 2,
        )
        self.body.position = (
            x - BODY_LENGTH / 2,
            foot_height + LEG_HEIGHT,
            z - BODY_WIDTH / 2,
        )
        self.left_arm.position = (
            x - BODY_LENGTH / 2 - ARM_LENGTH,
            foot_height + LEG_HEIGHT,
            z - BODY_WIDTH / 2,
        )
        self.right_arm.position = (
            x + BODY_LENGTH / 2,
            foot_height + LEG_HEIGHT,
            z - BODY_WIDTH / 2,
        )
        self.left_leg.position = (x - BODY_LENGTH / 2, foot_height, z - BODY_WIDTH / 2)
        self.right_leg.position = (
            x - BODY_LENGTH / 2 + LEG_LENGTH,
            foot_height,
            z - BODY_WIDTH / 2,
        )

    def update_rotation(self, xrot):  # here we must do some 3d rotation stuff
        drot = self.rotation - xrot
        self.update_rotation_relative(drot)

    def update_rotation_relative(self, drot):
        self.rotation += drot
        mx, my, mz = self.position
        for boxmodel in self.boxmodels:
            bx, by, bz = boxmodel.position
            rx, ry, rz = mx - bx, my - by, mz - bz
            xm = math.cos(drot) * rx + math.sin(drot) * rz
            ym = ry
            zm = math.cos(drot) * rz - math.sin(drot) * rx
            # boxmodel.position = (mx + xm, my + ym, mz + ym)
            rox, roy, roz = boxmodel.rotate_angle
            roy += drot
            boxmodel.rotate_angle = (rox, roy, roz)

    def draw(self):
        self.head.draw()
        self.body.draw()
        self.left_leg.draw()
        self.right_leg.draw()
        self.left_arm.draw()
        self.right_arm.draw()

    def getName(self):
        return "minecraft:player"

    def getDrop(self):
        return {}

    def getXP(self):
        return 0

    def update(self, dt):
        # self.update_rotation(G.window.rotation[1])
        pass


G.entityhandler.register(PlayerEntity)

G.entityhandler.add_entity("minecraft:player", (0, 0, 0))
