import globals as G
import log

class ICraftingInventory:
    """
    system for implementing an crafting-inventory
    must be included, not full InventoryClass
    """

    def getGridNames(self):
        """
        :return: a list of gridnames
        """
        raise NotImplementedError("in "+str(self)+".getGridNames("+str(self)+"): ICraftingInventory has not "+\
                                  "definited getGridNames()-method")

    def accessSlotsForGrid(self, grid):
        """
        function to get all possible slots used for an recipi in this grid. may empty if nothing
        :param grid: the grid name
        :return: a list of an list of slots
        """
        raise NotImplementedError("in "+str(self)+".accessSlotsForGrid("+str(self)+"): ICraftingInventory has not "+\
                                  "definited accessSlotsForGrid()-method")

    def writeOutputSlotsFor(self, grid, recipe):
        """
        function to set all slots for output for given grid and recipe.
        :param grid: the grid to use
        :param recipi: the recipi to use
        :return: if can be correct or not
        """
        raise NotImplementedError("in "+str(self)+".writeOutputSlotsFor("+str(self)+"): ICraftingInventory has not "+\
                                  "definited writeOutputSlotsFor()-method")

    def getOutputModeForGrid(self, grid, recipe):
        """
        function to get the mode for the outputs. modes: 0 -> recipe update, 1 -> ignore, 2 -> let stay
        :param grid: the grid
        :param recipe: the grid
        :return: an list of tupels of slot and mode
        """
        raise NotImplementedError("in "+str(self)+".getOutputModeForGrid("+str(self)+"): ICraftingInventory has not "+\
                                  "definited getOutputModeForGrid()-method")

    def recipiUpdate(self, byrecipe=None):
        """
        callen when the inventory is updated by recipe
        :param byrecipe: the recipi it is updated by
        """
        pass


class CraftingHandler:
    def __init__(self):
        self.typenames = []
        self.gridnames = [] # (name, type, mod)
        self.recipes = {} # name -> recipes

    def registerRecipeType(self, name, mod="minecraft"):
        """
        register a new recipi type
        :param name: the name of the type
        :param mod: the mod which is registrating. may be str
        """
        if (name, mod) in self.typenames: return
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
            self.recipes[type] = []

    def registerRecipeForGrid(self, gridname, recipeIn, recipeOut, recipeBy=None, recipeExtra=None):
        if not gridname in [x[0] for x in self.gridnames]:
            log.printMSG("[CRAFTINGHANDLER][ERROR] can't find grid named "+str(gridname))
            return
        self.recipes[gridname].append([recipeIn, recipeOut, recipeBy, recipeExtra])

G.craftinghandler = CraftingHandler()

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

# furnes recipe
G.craftinghandler.registerRecipeType("furnes")
G.craftinghandler.registerRecipeGrid("furnes", "1to1")







