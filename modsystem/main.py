import globals as G


class McPython(G.mod):
    def getName(self):
        """returns the name of the mod"""
        return "minecraft"

    def getVersion(self):
        """returns the version of the mod as tupel of three ints"""
        return (0, 0, G.VERSION_ID)

    def getUserFriendlyName(self):
        """function which returns the user-freindly name of the mod."""
        return "Mc Python"

G.modloader.register(McPython)