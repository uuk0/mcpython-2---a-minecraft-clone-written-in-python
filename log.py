import datetime

CASH = []

LINES = []

def getStamp():
    """returns a timestamp in string"""
    stamp = datetime.datetime.now()
    s = ""
    s += "["+str(stamp.year)+"]"
    s += "["+str(stamp.month)+" "*(2-len(str(stamp.month)))+"]"
    s += "["+str(stamp.day)+" "*(2-len(str(stamp.day)))+"]"
    s += "["+str(stamp.hour)+" "*(2-len(str(stamp.hour)))+"]"
    s += "["+str(stamp.minute)+" "*(2-len(str(stamp.minute)))+"]"
    s += "["+str(stamp.second)+" "*(2-len(str(stamp.second)))+"]"
    return s



def printMSG(*msg, end="\n"):
    """
    print an message with a timestamp into the chat
    :param msg: the message which should be printed out
    """
    stamp = getStamp()
    _print(stamp, *msg, end=end)
    CASH.append([stamp] + list([str(e) for e in msg]))
    LINES.append([stamp, msg])

global print
_print = print
print = printMSG
