

class ICraftingInventory:
    """
    system for implementing an crafting-inventory
    must be included, not full InventoryClass
    """

    def __init__(self):
        """
        MUST be callen by __init__ by master
        """
        self.active_recipe = None

    def get_grid_names(self) -> list:
        """
        :return: a list of grids to check. will call get_slot_arrays(gridname) and point it ti check_recipes(
        """
        return []

    def check_recipes(self, recipelist: list, slotlist: list):
        """
        returns if ANY recgistrated recipe equals the slotlist & gridtype
        :param recipelist: the list of recipe to check
        :param slotlist: the slots that should be used
        :param grid: the grid the slots are in
        :return: an recipe object or None for the equal recipe
        """
        return None

    def get_slot_arrays(self, gridname: str) -> list:
        """
        :return: a list of lists of slots for the possible slots
        """
        return []

    def get_output_for_recipe(self, recipe):
        """
        :param recipe: the recipe the output is for
        :return: anything or None as provided for output
        """
        return None

    def set_output(self, output):
        """
        :param output: the output to set
        :return: weither the output is valid or not
        """
        pass

    def clear_output(self):
        """
        clear the output of the crafting grid
        """

    def on_output_remove(self, slot):
        """
        callen when one slot of the output slots is changed. IS NOT AUTOMATICLY REGISTERED
        -> need an own binding to Slot-object
        """

    def on_input_remove(self, slot):
        """
        callen when one slot of the input slots is changed. IS NOT AUTOMATICLY REGISTERED
        -> need an own binding to Slot-object
        """

