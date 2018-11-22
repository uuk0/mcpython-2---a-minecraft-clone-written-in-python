import os

import config
import globals as G
import log
import texturhandler


class TextureDataHandler:
    def __init__(self):
        self.texturs = {}
        self.block_dirs = [G.local+"assets/textures/block/"]

    def addForBlock(self, name, filelist, type=0):
        if config.DEBUG.PRINT_TEXTURDATAHANDLER_STUFF:
            log.printMSG("[TEXTURDATAHANDLER][INFO] registrating block textur named "+str(name))
        for i, e in enumerate(filelist[:]):
            if not os.path.isfile(e):
                flag = True
                index = 0
                while flag and index < len(self.block_dirs):
                    if os.path.isfile(self.block_dirs[index]+e):
                        filelist[i] = self.block_dirs[index]+e
                        flag = False
        if len(filelist) == 1:
            texturhandler.resize(filelist[0], (64, 64))
            self.texturs[name] = filelist[0]
        else:
            texturhandler.storetexturs(G.local+"tmp/"+name+".png", filelist)
            self.texturs[name] = G.local+"tmp/"+name+".png"
        if type == 0:
            G.texturhandler.registerBlockTextur(self.texturs[name])
        elif type == 1:
            G.texturhandler.registerBoxModelTextur(self.texturs[name])


G.texturedatahandler = TextureDataHandler()

def loadTexturs(*args):

    os.makedirs(G.local+"tmp/minecraft")

    G.texturedatahandler.addForBlock("minecraft/bedrock", ["bedrock.png"])
    G.texturedatahandler.addForBlock("minecraft/brick",   ["bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/cactus",
                                     ["cactus_bottom.png", "cactus_side.png", "cactus_top.png"], type=1)
    G.texturedatahandler.addForBlock("minecraft/dirt", ["dirt.png"])
    G.texturedatahandler.addForBlock("minecraft/grass",
                                     ["grass_block_side.png", "dirt.png", "grass_top_colored.png"])
    G.texturedatahandler.addForBlock("minecraft/acacia_leave", ["acacia_leaves.png"])
    G.texturedatahandler.addForBlock("minecraft/acacia_log",
                                     ["acacia_log.png", "acacia_log_top.png", "acacia_log_rotated.png"])
    G.texturedatahandler.addForBlock("minecraft/obsidian", ["obsidian.png"])
    G.texturedatahandler.addForBlock("minecraft/coal_ore", ["coal_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/diamond_ore", ["diamond_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/emerald_ore", ["emerald_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/gold_ore", ["gold_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/iron_ore", ["iron_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/lapis_ore", ["lapis_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/nether_quartz_ore", ["nether_quartz_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/redstone_ore", ["redstone_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/sand", ["sand.png"])
    G.texturedatahandler.addForBlock("minecraft/stone", ["stone.png"])
    G.texturedatahandler.addForBlock("minecraft/cobbelstone", ["cobblestone.png"])
    G.texturedatahandler.addForBlock("minecraft/crafting_table",
                                     ["crafting_table_front.png", "crafting_table_side.png", "crafting_table_top.png",
                                      "oak_planks.png"])
    G.texturedatahandler.addForBlock("minecraft/acacia_plank", ["acacia_planks.png"])
    G.texturedatahandler.addForBlock("minecraft/stone_brick", ["stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/mossy_stone_brick", ["mossy_stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/cracked_stone_brick", ["cracked_stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/chiseled_stone_brick", ["chiseled_stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/mossy_cobbelstone", ["mossy_cobblestone.png"])
    G.texturedatahandler.addForBlock("minecraft/gravel", ["gravel.png"])
    G.texturedatahandler.addForBlock("minecraft/coal_block", ["coal_block.png"])
    G.texturedatahandler.addForBlock("minecraft/diamond_block", ["diamond_block.png"])
    G.texturedatahandler.addForBlock("minecraft/emerald_block", ["emerald_block.png"])
    G.texturedatahandler.addForBlock("minecraft/gold_block", ["gold_block.png"])
    G.texturedatahandler.addForBlock("minecraft/iron_block", ["iron_block.png"])
    G.texturedatahandler.addForBlock("minecraft/lapis_block", ["lapis_block.png"])
    G.texturedatahandler.addForBlock("minecraft/quartz_block",
                                     ["quartz_block_bottom.png", "quartz_block_side.png", "quartz_block_top.png"])
    G.texturedatahandler.addForBlock("minecraft/chiseled_quartz_block", ["chiseled_quartz_block.png",
                                                                         "chiseled_quartz_block_top.png"])
    G.texturedatahandler.addForBlock("minecraft/quartz_pillar", ["quartz_pillar.png", "quartz_pillar_top.png"])
    G.texturedatahandler.addForBlock("minecraft/redstone_block", ["redstone_block.png"])
    G.texturedatahandler.addForBlock("minecraft/andesite", ["andesite.png"])
    G.texturedatahandler.addForBlock("minecraft/polished_andesite", ["polished_andesite.png"])
    G.texturedatahandler.addForBlock("minecraft/granite", ["granite.png"])
    G.texturedatahandler.addForBlock("minecraft/polished_granite", ["polished_granite.png"])
    G.texturedatahandler.addForBlock("minecraft/diorite", ["diorite.png"])
    G.texturedatahandler.addForBlock("minecraft/polished_diorite", ["polished_diorite.png"])
    G.texturedatahandler.addForBlock("minecraft/endstone", ["end_stone.png"])
    G.texturedatahandler.addForBlock("minecraft/endstone_brick", ["end_stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/birch_log",
                                     ["birch_log.png", "birch_log_top.png", "birch_log_rotated.png"])
    G.texturedatahandler.addForBlock("minecraft/ice", ["ice.png"])
    G.texturedatahandler.addForBlock("minecraft/packed_ice", ["packed_ice.png"])
    G.texturedatahandler.addForBlock("minecraft/blue_ice", ["blue_ice.png"])
    G.texturedatahandler.addForBlock("minecraft/barrel", ["barrel_bottom.png", "barrel_side.png", "barrel_top.png"])
    G.texturedatahandler.addForBlock("minecraft/birch_plank", ["birch_planks.png"])
    G.texturedatahandler.addForBlock("minecraft/glowstone", ["glowstone.png"])
    G.texturedatahandler.addForBlock("minecraft/redsand", ["red_sand.png"])
    G.texturedatahandler.addForBlock("minecraft/sandstone",
                                     ["sandstone.png", "sandstone_bottom.png", "sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/chiseled_sandstone",
                                     ["chiseled_sandstone.png", "sandstone_bottom.png", "sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/cut_sandstone",
                                     ["cut_sandstone.png", "sandstone_bottom.png","sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/red_sandstone",
                                     ["red_sandstone.png", "red_sandstone_bottom.png","red_sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/red_chiseled_sandstone",
                                     ["chiseled_red_sandstone.png", "red_sandstone_bottom.png", "red_sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/red_cut_sandstone",
                                     ["cut_red_sandstone.png", "red_sandstone_bottom.png", "red_sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/tnt", ["tnt_bottom.png", "tnt_side.png", "tnt_top.png"])
    G.texturedatahandler.addForBlock("minecraft/redstone_lamp", ["redstone_lamp.png", "redstone_lamp_on.png"])
    G.texturedatahandler.addForBlock("minecraft/white_wool", ["white_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/orange_wool", ["orange_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/magenta_wool", ["magenta_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/light_blue_wool", ["light_blue_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/yellow_wool", ["yellow_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/lime_wool", ["lime_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/pink_wool", ["pink_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/gray_wool", ["gray_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/light_gray_wool", ["light_gray_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/cyan_wool", ["cyan_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/purple_wool", ["purple_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/blue_wool", ["blue_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/brown_wool", ["brown_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/green_wool", ["green_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/red_wool", ["red_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/black_wool", ["black_wool.png"])
    G.texturedatahandler.addForBlock("minecraft/redstone_wire", ["redstone_block.png"])
    G.texturedatahandler.addForBlock("minecraft/oak_log", ["oak_log.png", "oak_log_top.png", "oak_log_rotated.png"])
    #G.texturedatahandler.addForBlock("minecraft/stripped_oak_log", ["stripped_oak_log.png", "stripped_oak_log_top.png", "stripped_oak_log_rotated.png"])

G.eventhandler.on_event("game:registry:on_texture_registrate_periode", loadTexturs)