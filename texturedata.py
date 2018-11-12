import globals as G
import texturhandler
import log
import os
import config

class TextureDataHandler:
    def __init__(self):
        self.texturs = {}

    def addForBlock(self, name, filelist, type=0):
        if config.DEBUG.PRINT_TEXTURDATAHANDLER_STUFF:
            log.printMSG("[TEXTURDATAHANDLER][INFO] registrating block textur named "+str(name))
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
    G.texturedatahandler.addForBlock("minecraft/bedrock", [G.local+"assets/textures/block/bedrock.png"])
    G.texturedatahandler.addForBlock("minecraft/brick",   [G.local+"assets/textures/block/bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/cactus",  [G.local+"assets/textures/block/cactus_bottom.png",
                                                           G.local+"assets/textures/block/cactus_side.png",
                                                           G.local+"assets/textures/block/cactus_top.png"], type=1)
    G.texturedatahandler.addForBlock("minecraft/dirt",    [G.local+"assets/textures/block/dirt.png"])
    G.texturedatahandler.addForBlock("minecraft/grass",   [G.local+"assets/textures/block/grass_block_side.png",
                                                           G.local+"assets/textures/block/dirt.png",
                                                           G.local+"assets/textures/block/grass_top_colored.png"])
    G.texturedatahandler.addForBlock("minecraft/acacia_leave", [G.local+"assets/textures/block/acacia_leaves.png"])
    G.texturedatahandler.addForBlock("minecraft/acacia_log", [G.local+"assets/textures/block/acacia_log.png",
                                                              G.local+"assets/textures/block/acacia_log_top.png",
                                                              G.local+"assets/textures/block/acacia_log_rotated.png"])
    G.texturedatahandler.addForBlock("minecraft/obsidian", [G.local+"assets/textures/block/obsidian.png"])
    G.texturedatahandler.addForBlock("minecraft/coal_ore", [G.local+"assets/textures/block/coal_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/diamond_ore", [G.local+"assets/textures/block/diamond_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/emerald_ore", [G.local+"assets/textures/block/emerald_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/gold_ore", [G.local+"assets/textures/block/gold_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/iron_ore", [G.local+"assets/textures/block/iron_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/lapis_ore", [G.local+"assets/textures/block/lapis_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/nether_quartz_ore", [G.local+"assets/textures/block/nether_quartz_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/redstone_ore", [G.local+"assets/textures/block/redstone_ore.png"])
    G.texturedatahandler.addForBlock("minecraft/sand", [G.local+"assets/textures/block/sand.png"])
    G.texturedatahandler.addForBlock("minecraft/stone", [G.local+"assets/textures/block/stone.png"])
    G.texturedatahandler.addForBlock("minecraft/cobbelstone", [G.local+"assets/textures/block/cobblestone.png"])

    G.texturedatahandler.addForBlock("minecraft/crafting_table", [G.local+"assets/textures/block/crafting_table_front.png",
                                                                  G.local+"assets/textures/block/crafting_table_side.png",
                                                                  G.local+"assets/textures/block/crafting_table_top.png",
                                                                  G.local+"assets/textures/block/oak_planks.png"])
    G.texturedatahandler.addForBlock("minecraft/acacia_plank", [G.local+"assets/textures/block/acacia_planks.png"])
    G.texturedatahandler.addForBlock("minecraft/stone_brick", [G.local+"assets/textures/block/stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/mossy_stone_brick", [G.local+"assets/textures/block/mossy_stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/cracked_stone_brick", [G.local+"assets/textures/block/cracked_stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/chiseled_stone_brick", [G.local+"assets/textures/block/chiseled_stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/mossy_cobbelstone", [G.local+"assets/textures/block/mossy_cobblestone.png"])
    G.texturedatahandler.addForBlock("minecraft/gravel", [G.local+"assets/textures/block/gravel.png"])
    G.texturedatahandler.addForBlock("minecraft/coal_block", [G.local+"assets/textures/block/coal_block.png"])
    G.texturedatahandler.addForBlock("minecraft/diamond_block", [G.local+"assets/textures/block/diamond_block.png"])
    G.texturedatahandler.addForBlock("minecraft/emerald_block", [G.local+"assets/textures/block/emerald_block.png"])
    G.texturedatahandler.addForBlock("minecraft/gold_block", [G.local+"assets/textures/block/gold_block.png"])
    G.texturedatahandler.addForBlock("minecraft/iron_block", [G.local+"assets/textures/block/iron_block.png"])
    G.texturedatahandler.addForBlock("minecraft/lapis_block", [G.local+"assets/textures/block/lapis_block.png"])
    G.texturedatahandler.addForBlock("minecraft/quartz_block", [G.local+"assets/textures/block/quartz_block_bottom.png",
                                                                G.local+"assets/textures/block/quartz_block_side.png",
                                                                G.local+"assets/textures/block/quartz_block_top.png"])
    G.texturedatahandler.addForBlock("minecraft/chiseled_quartz_block", [G.local+"assets/textures/block/chiseled_quartz_block.png",
                                                                         G.local+"assets/textures/block/chiseled_quartz_block_top.png"])
    G.texturedatahandler.addForBlock("minecraft/quartz_pillar", [G.local+"assets/textures/block/quartz_pillar.png",
                                                                 G.local+"assets/textures/block/quartz_pillar_top.png"])
    G.texturedatahandler.addForBlock("minecraft/redstone_block", [G.local+"assets/textures/block/redstone_block.png"])
    G.texturedatahandler.addForBlock("minecraft/andesite", [G.local+"assets/textures/block/andesite.png"])
    G.texturedatahandler.addForBlock("minecraft/polished_andesite", [G.local+"assets/textures/block/polished_andesite.png"])
    G.texturedatahandler.addForBlock("minecraft/granite", [G.local+"assets/textures/block/granite.png"])
    G.texturedatahandler.addForBlock("minecraft/polished_granite", [G.local+"assets/textures/block/polished_granite.png"])
    G.texturedatahandler.addForBlock("minecraft/diorite", [G.local+"assets/textures/block/diorite.png"])
    G.texturedatahandler.addForBlock("minecraft/polished_diorite", [G.local+"assets/textures/block/polished_diorite.png"])
    G.texturedatahandler.addForBlock("minecraft/endstone", [G.local+"assets/textures/block/end_stone.png"])
    G.texturedatahandler.addForBlock("minecraft/endstone_brick", [G.local+"assets/textures/block/end_stone_bricks.png"])
    G.texturedatahandler.addForBlock("minecraft/birch_log", [G.local+"assets/textures/block/birch_log.png",
                                                             G.local+"assets/textures/block/birch_log_top.png",
                                                             G.local+"assets/textures/block/birch_log_rotated.png"])
    G.texturedatahandler.addForBlock("minecraft/ice", [G.local+"assets/textures/block/ice.png"])
    G.texturedatahandler.addForBlock("minecraft/packed_ice", [G.local+"assets/textures/block/packed_ice.png"])
    G.texturedatahandler.addForBlock("minecraft/blue_ice", [G.local+"assets/textures/block/blue_ice.png"])
    G.texturedatahandler.addForBlock("minecraft/barrel", [G.local+"assets/textures/block/barrel_bottom.png",
                                                          G.local+"assets/textures/block/barrel_side.png",
                                                          G.local+"assets/textures/block/barrel_top.png"])
    G.texturedatahandler.addForBlock("minecraft/birch_plank", [G.local+"assets/textures/block/birch_planks.png"])
    G.texturedatahandler.addForBlock("minecraft/glowstone", [G.local+"assets/textures/block/glowstone.png"])
    G.texturedatahandler.addForBlock("minecraft/redsand", [G.local+"assets/textures/block/red_sand.png"])
    G.texturedatahandler.addForBlock("minecraft/sandstone", [G.local+"assets/textures/block/sandstone.png",
                                                             G.local+"assets/textures/block/sandstone_bottom.png",
                                                             G.local+"assets/textures/block/sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/chiseled_sandstone", [G.local+"assets/textures/block/chiseled_sandstone.png",
                                                                      G.local+"assets/textures/block/sandstone_bottom.png",
                                                                      G.local+"assets/textures/block/sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/cut_sandstone", [G.local+"assets/textures/block/cut_sandstone.png",
                                                                 G.local+"assets/textures/block/sandstone_bottom.png",
                                                                 G.local+"assets/textures/block/sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/red_sandstone", [G.local+"assets/textures/block/red_sandstone.png",
                                                                 G.local+"assets/textures/block/red_sandstone_bottom.png",
                                                                 G.local+"assets/textures/block/red_sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/red_chiseled_sandstone",
                                     [G.local+"assets/textures/block/chiseled_red_sandstone.png",
                                      G.local+"assets/textures/block/red_sandstone_bottom.png",
                                      G.local+"assets/textures/block/red_sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/red_cut_sandstone",
                                     [G.local+"assets/textures/block/cut_red_sandstone.png",
                                      G.local + "assets/textures/block/red_sandstone_bottom.png",
                                      G.local + "assets/textures/block/red_sandstone_top.png"])
    G.texturedatahandler.addForBlock("minecraft/tnt", [G.local+"assets/textures/block/tnt_bottom.png",
                                                       G.local+"assets/textures/block/tnt_side.png",
                                                       G.local+"assets/textures/block/tnt_top.png"])
    G.texturedatahandler.addForBlock("minecraft/redstone_lamp", [G.local+"assets/textures/block/redstone_lamp.png",
                                                                 G.local+"assets/textures/block/redstone_lamp_on.png"])

G.eventhandler.on_event("game:registry:on_texture_registrate_periode", loadTexturs)