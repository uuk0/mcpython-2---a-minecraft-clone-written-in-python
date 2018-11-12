import datetime

"""returns a timestamp in string"""
def getStamp():
    stamp = datetime.datetime.now()
    s = ""
    s += "["+str(stamp.year)+"]"
    s += "["+str(stamp.month)+" "*(2-len(str(stamp.month)))+"]"
    s += "["+str(stamp.day)+" "*(2-len(str(stamp.day)))+"]"
    s += "["+str(stamp.hour)+" "*(2-len(str(stamp.hour)))+"]"
    s += "["+str(stamp.minute)+" "*(2-len(str(stamp.minute)))+"]"
    s += "["+str(stamp.second)+" "*(2-len(str(stamp.second)))+"]"
    return s

"""print an message with a timestamp into the chat"""
def printMSG(msg):
    if not str(msg).startswith("[") or str(msg).startswith("[["): return
    print(getStamp()+str(msg))
