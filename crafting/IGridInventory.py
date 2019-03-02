import crafting.ICraftingInventory
import globals as G


def _sum_slotarray(slotarray):
    if len(slotarray) == 0 or type(slotarray[0]) != list:
        return slotarray
    array = []
    for e in slotarray:
        array += e
    return array


class IGridInventory(crafting.ICraftingInventory.ICraftingInventory):
    """
    base class for all crafting-grid-inventorys
    """

    def __init__(self):
        crafting.ICraftingInventory.ICraftingInventory.__init__(self)

    def get_grid_size(self):
        """
        :return: the size of the grid as an tuple of (x, y)
        """
        return (0, 0)

    def get_spezial_prefix(self):
        """
        :return: an spezial prefix for all gridnames
        """
        return "crafting_base"

    def get_output_size(self):
        """
        :return: the size of the output as an tuple of (x, y)
        """
        return (1, 1)

    def get_input_slots(self):
        """
        :return: returns an list of lists of inputslots as an gridarray
        """
        return []

    def get_output_slots(self):
        """
        :return:  returns an list of lists of outputslots as an gridarray
        """
        return []

    ###################################################################################
    # special grid info - do NOT overwrite them otherwise you know what you are doing #
    ###################################################################################

    def get_grid_names(self):
        sx, sy = self.get_grid_size()
        array = []
        for x in range(1, sx+1):
            for y in range(1, sy+1):
                array.append(self.get_spezial_prefix()+"|"+str(x)+"x"+str(y))
        return array

    def get_slot_arrays(self, gridname):
        array = []
        x, y = gridname.split("|")[1].split("x")
        x, y = int(x), int(y)
        slots = self.get_input_slots()
        sx, sy = len(slots), len(slots[0])
        for mx in range(sx-x):
            for my in range(sy-y):
                subarray = []
                for ix in range(x):
                    for iy in range(y):
                        subarray.append(slots[mx+ix][my+iy])
                array.append(subarray)
        return array

    def check_recipes(self, recipelist: list, slotlist: list):
        for recipe in recipelist:
            if self._check_recipe(recipe, slotlist):
                return recipe
        return None

    def _check_recipe(self, recipe, slotlist) -> bool:
        arrayslot = _sum_slotarray(slotlist)
        arrayneed = _sum_slotarray(recipe.inputs)
        for i, slot in enumerate(arrayslot):
            need = arrayneed[i]
            itemname = slot.stack.item.getName() if slot.stack and slot.stack.item else None
            if not ((not (itemname and need)) or (itemname == need or any([
                     x.getName(None) == itemname for x in G.notationhandler.getnotatedobjectsfor(need)]))):
                return False
        self.active_recipe = (recipe, arrayslot)
        return True

    def get_output_for_recipe(self, recipe):
        return recipe.outputs

    def set_output(self, output):
        array_slot = _sum_slotarray(self.get_output_slots())
        array_todo = _sum_slotarray(output)
        for i, slot in enumerate(array_slot):
            slot.setItem(array_todo[i]["item"], array_todo[i]["amount"])

    def clear_output(self):
        for slot in self.get_output_slots():
            slot.setItem(None)

    def add_input(self, position):
        """
        adds an new Slot to the inventorysystem. returns the slot
        :param position: the position to set to
        """
        return G.inventoryslot(position, update_func=self.on_input_remove)

    def add_output(self, position):
        """
        adds an new Slot to the inventorysystem. returns the slot
        :param position: the position to set to
        """
        return G.inventoryslot(position, update_func=self.on_output_remove, canplayersetitems=False)

    def on_output_remove(self, output_slot):
        if not self.active_recipe:
            return
        if output_slot.stack.item:
            return
        input_slots = self.active_recipe[1]
        for i, inputslot in enumerate(input_slots):
            if inputslot.stack:
                inputslot.stack.amount -= 1
                if inputslot.stack.amount == 0:
                    inputslot.setItem(None, 0)
        G.craftinghandler.check_inventory(self)

    def _remove_input_1(self):
        recipe, input_slots = self.active_recipe
        for i, slot in enumerate(input_slots):
            if slot.stack:
                slot.stack.amount -= 1
                if slot.stack.amount == 0:
                    slot.setItem(None)
        # simple checking if the recipi is still active
        G.craftinghandler.check_inventory(self)

    def on_input_remove(self, slot):
        G.craftinghandler.check_inventory(self)


