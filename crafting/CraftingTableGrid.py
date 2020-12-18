import globals as G

# basic crafting recipis in grids

G.craftinghandler.registerRecipeType("crafting_base")

# nxn-grids has optional 'extra' attribute mirroded

G.craftinghandler.registerRecipeGrid("crafting_base", "1x1")
G.craftinghandler.registerRecipeGrid("crafting_base", "1x2")
G.craftinghandler.registerRecipeGrid("crafting_base", "1x3")
G.craftinghandler.registerRecipeGrid("crafting_base", "2x1")
G.craftinghandler.registerRecipeGrid("crafting_base", "2x2")
G.craftinghandler.registerRecipeGrid("crafting_base", "2x3")
G.craftinghandler.registerRecipeGrid("crafting_base", "3x1")
G.craftinghandler.registerRecipeGrid("crafting_base", "3x2")
G.craftinghandler.registerRecipeGrid("crafting_base", "3x3")
G.craftinghandler.registerRecipeGrid("crafting_base", "shapeless")
