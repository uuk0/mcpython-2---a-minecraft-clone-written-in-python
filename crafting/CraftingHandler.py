import crafting.ICraftingInventory
import crafting.Recipe
import globals as G
import log


class CraftingHandler:
    def __init__(self):
        self.typenames = []
        self.gridnames = []  # (name, type, mod)
        self.recipes = {}  # name -> recipes

    def registerRecipeType(self, name, mod="minecraft"):
        """
        register a new recipi type
        :param name: the name of the type
        :param mod: the mod which is registrating. may be str
        """
        if (name, mod) in self.typenames:
            return
        self.typenames.append((name, mod))

    def registerRecipeGrid(self, type, name):
        """
        register a new recipi grid
        :param type: the type of the recipe grid
        :param name:
        :return:
        """
        typeinfo = None
        for e in self.typenames:
            if e[0] == type:
                typeinfo = e
        if (name, typeinfo[0], typeinfo[1]) not in self.gridnames:
            self.gridnames.append((name, typeinfo[0], typeinfo[1]))
            self.recipes[typeinfo[0] + "|" + name] = []

    def registerRecipe(self, recipe):
        self.recipes[recipe.gridname].append(recipe)

    def check_inventory(self, inventory):
        if not issubclass(
            type(inventory), crafting.ICraftingInventory.ICraftingInventory
        ):
            log.printMSG(
                "[CRAFTINGHANDLER][INFO] can't check inventory "
                + str(inventory)
                + ". Inventory is not an crafting inventory"
            )
            return
        inventory.active_recipe = None
        for e in inventory.get_grid_names():
            for slotarray in inventory.get_slot_arrays(e):
                recipe = inventory.check_recipes(self.recipes[e], slotarray)
                if recipe:
                    inventory.set_output(inventory.get_output_for_recipe(recipe))
                    return
        inventory.clear_output()


G.craftinghandler = CraftingHandler()

from crafting import CraftingTableGrid, FurnesGrid

G.craftinghandler.registerRecipe(
    crafting.Recipe.Recipe(
        "crafting_base|2x2",
        [["minecraft:grass"] * 2] * 2,
        [[{"item": "minecraft:dirt", "amount": 4}]],
    )
)
