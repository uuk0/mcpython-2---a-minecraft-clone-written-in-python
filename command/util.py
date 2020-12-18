def parseStringPosition(x, y, z, executeposition):
    if "~" in x:
        if len(x) == 1:
            x = executeposition[0]
        else:
            x = executeposition[0] + float(x[1:])
    if "~" in y:
        if len(y) == 1:
            y = executeposition[1]
        else:
            y = executeposition[1] + float(y[1:])
    if "~" in z:
        if len(z) == 1:
            z = executeposition[2]
        else:
            z = executeposition[2] + float(z[1:])
    return x, y, z
