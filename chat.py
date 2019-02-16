import clipboard
import pyglet
from pyglet.window import key

import config
import globals as G
import log

"""
list of keys
cotains dicts for: without, with SHIFT, with ALT_GR

automated convert upper-makeable strings in KEYDICT[0] to upper in KEYDICT[1]
"""
KEYDICT = [{key.A:"a", key.B:"b", key.C:"c", key.D:"d", key.E:"e", key.F:"f", key.G:"g", key.H:"h", key.I:"i", key.J:"j",
            key.K:"k", key.L:"l", key.M:"m", key.N:"n", key.O:"o", key.P:"p", key.Q:"q", key.R:"r", key.S:"s", key.T:"t",
            key.U:"u", key.V:"v", key.W:"w", key.X:"x", key.Y:"y", key.Z:"z", key._0:"0", key._1:"1", key._2:"2",
            key._3:"3", key._4:"4", key._5:"5", key._6:"6", key._7:"7", key._8:"8", key._9:"9", key.PLUS:"+", key.MINUS:"-",
            35:"#", 940597837824:"ß", 949187772416:"´", 944892805120:"^", 44:",", 46:".", 60:"-", 32:" "},
           {key._1:"!", key._2:'"', key._3:"§", key._4:"$", key._5:"%", key._6:"&", key._7:"/", key._8:"(", key._9:")",
            key._0:"=", 35:"'", 940597837824:"?", 949187772416:"`", 944892805120:"°", 44:";", 46:":", 45:"_"},
           {key.Q:"@", key.E:"€", key.M:"µ", key._7:"{", key._8:"[", key._9:"]", key._0:"}", key.PLUS:"~",
            940597837824:"\\"}]

for e in KEYDICT[0].keys():
    if KEYDICT[0][e].upper() != KEYDICT[0][e] and e not in [940597837824]:
        KEYDICT[1][e] = KEYDICT[0][e].upper()

"""class for chat"""
class chat(G.inventoryclass):
    def __init__(self):
        G.inventoryclass.__init__(self)
        G.chat = self
        self.text = ""
        self.lable = pyglet.text.Label('', font_name='Arial', font_size=18,
            x=10, y=30, anchor_x='left', anchor_y='top',
            color=(0, 0, 0, 255))

    """draws the chat. only used by eventhandler"""
    def draw(self):
        self.lable.text = self.text
        self.lable.draw()

    """adds an key to chat. only used by eventhandler"""
    def on_key_press(self, symbol, modifiers):
        G.window.strafe = [0, 0]
        if symbol in [65505]: return
        elif symbol == config.Keyboard.CLOSE:
            self.text = ""
            G.inventoryhandler.hide_inventory(self.id)
        elif symbol == config.Keyboard.RUN_COMMAND:
            self.execute(self.text)
            self.text = ""
            G.inventoryhandler.hide_inventory(self.id)
        elif symbol == 65288:
            self.text = self.text[:-1]
        elif (modifiers & key.MOD_SHIFT):
            if symbol in KEYDICT[1]:
                self.text += KEYDICT[1][symbol]
            else:
                log.printMSG("[CHAT][ERROR] can't interpet key " + str(symbol)+" with SHIFT")
        elif (modifiers & key.MOD_ALT):
            if symbol in KEYDICT[2]:
                self.text += KEYDICT[2][symbol]
            else:
                log.printMSG("[CHAT][ERROR] can't interpet key " + str(symbol)+" with ALT")
        elif symbol in KEYDICT[0]:
            self.text += KEYDICT[0][symbol]
        elif symbol == 65507 and modifiers & 18:
            clipboard.copy(self.text)
        elif symbol == key.V and modifiers & 18:
            self.text += clipboard.paste()
        elif symbol == key.D and modifiers & 18:
            self.text = ""
        elif symbol == key.TAB:
            log.printMSG("[CHAT][WARN] complet of commands are not supported")
        else:
            log.printMSG("[CHAT][ERROR] can't interpet key "+str(symbol)+" with modifiers: "+str(modifiers))
        G.window.strafe = [0, 0]

    """execute an command"""
    def execute(self, command):
        splitted = command.split(" ")
        if len(command) > 0 and command[0] != "/":
            log.printMSG("[CHAT] "+command)
            return
        else:
            G.commandhandler.executeCommand(command, G.player.entity, G.window.position)
            return

    """print a line to the chat
    color is not used at the moment"""
    def printLine(self, string, color=(0, 0, 0)):
        log.printMSG("[CHAT] "+str(string))


