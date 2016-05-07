from string import maketrans

def replaceNew(originalString):
    instr = "abcdefghijklmnopqrstuvwxyz"
    outstr= "cdefghijklmnopqrstuvwxyzab"

    t = maketrans(instr, outstr)

    return originalString.translate(t)


print replaceNew("http://www.pythonchallenge.com/pc/def/map.html")
