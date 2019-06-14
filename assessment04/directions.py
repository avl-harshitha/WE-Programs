def nextpoint(lattpnt, dir, magnitude):
    dirdict = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
    distance = [magnitude * i for i in dirdict[dir]]
    return [(x+y) for x, y in zip(lattpnt, distance)]


def terminus(lattpnt, directionlist):
    destination = list(lattpnt)
    for dir in directionlist:
        for singledir in dir[1:]:
            destination = nextpoint(destination, singledir, int(dir[0]))
    return destination


print(terminus((-1, 1), ["1NE"]))

